// Annotation layer for manual screenshots: red boxes, arrows and numbered callouts
// drawn as an SVG overlay at the real positions of page elements, then captured.
//
// spec (per target, key "annotate"):
//   { box:   [locator...], pad?: 4 }                 red rectangle around the union of elements
//   { arrow: { from: locator, to: locator, fromSide?: 'bottom'|'right'|..., toSide?: 'top'|'left'|..., elbow?: 'v'|'h' } }
//   { callout: { target: locator, label: '59', side?: 'below'|'above'|'right'|'left', dist?: 34,
//                dx?, dy? (shift the label), ax?, ay? (shift the arrow tip), straight?: true (keep arrow axis-aligned) } }
//   box also takes minX?/maxX? (clamp the frame horizontally, page px), color?: 'blue' (callout-style frame) and width? (stroke width)
// and optional "crop": { around: [locator...], pad: 24 } to clip the screenshot.
// A locator is a Playwright selector string, e.g. "text=参加リクエスト >> visible=true".

const RED = '#ff0000';
const BLUE = '#0b6fb8';

async function bbox(page, sel) {
  const loc = page.locator(sel).first();
  await loc.waitFor({ state: 'visible', timeout: 15000 });
  const b = await loc.boundingBox();
  const sx = await page.evaluate(() => window.scrollX);
  const sy = await page.evaluate(() => window.scrollY);
  return { x: b.x + sx, y: b.y + sy, w: b.width, h: b.height };
}

function union(bs, pad = 0) {
  const x1 = Math.min(...bs.map(b => b.x)) - pad, y1 = Math.min(...bs.map(b => b.y)) - pad;
  const x2 = Math.max(...bs.map(b => b.x + b.w)) + pad, y2 = Math.max(...bs.map(b => b.y + b.h)) + pad;
  return { x: x1, y: y1, w: x2 - x1, h: y2 - y1 };
}

function side(b, s) {
  switch (s) {
    case 'top': return [b.x + b.w / 2, b.y];
    case 'left': return [b.x, b.y + b.h / 2];
    case 'right': return [b.x + b.w, b.y + b.h / 2];
    default: return [b.x + b.w / 2, b.y + b.h];
  }
}

async function annotate(page, specs) {
  const shapes = [];   // drawing primitives in document coordinates
  const extents = [];  // for cropping
  const boxes = {};
  for (const s of specs) {
    if (s.box) {
      const u = union(await Promise.all(s.box.map(sel => bbox(page, sel))), s.pad ?? 4);
      if (s.minX != null && u.x < s.minX) { u.w -= s.minX - u.x; u.x = s.minX; }      // keep the frame off e.g. the side menu
      if (s.maxX != null && u.x + u.w > s.maxX) u.w = s.maxX - u.x;
      shapes.push({ t: 'rect', ...u, color: s.color === 'blue' ? BLUE : (s.color || RED), width: s.width });
      extents.push(u);
      if (s.id) boxes[s.id] = u;
    } else if (s.arrow) {
      const a = s.arrow;
      const fb = boxes[a.from] || union([await bbox(page, a.from)], 4);
      const tb = boxes[a.to] || union([await bbox(page, a.to)], 4);
      const p1 = side(fb, a.fromSide || 'bottom'), p2 = side(tb, a.toSide || 'top');
      if (a.at) { p1[0] = fb.x + fb.w * a.at; }            // anchor x as a fraction of the from-box width
      if (a.straight === 'v') p2[0] = p1[0];               // keep the arrow vertical
      if (a.straight === 'h') p2[1] = p1[1];               // keep the arrow horizontal
      let pts = [p1, p2];
      if (a.elbow === 'v') pts = [p1, [p1[0], p2[1]], p2];        // go vertical, then horizontal
      if (a.elbow === 'h') pts = [p1, [p2[0], p1[1]], p2];        // go horizontal, then vertical
      shapes.push({ t: 'arrow', pts, color: RED });
    } else if (s.callout) {
      const c = s.callout, tb = await bbox(page, c.target);
      const d = c.dist ?? 34, W = 46, H = 32;
      let bx, by, p1, p2;
      if (c.side === 'above') { bx = tb.x + tb.w / 2 - W / 2; by = tb.y - d - H; p1 = [tb.x + tb.w / 2, by + H]; p2 = [tb.x + tb.w / 2, tb.y]; }
      else if (c.side === 'left') { bx = tb.x - d - W; by = tb.y + tb.h / 2 - H / 2; p1 = [bx + W, by + H / 2]; p2 = [tb.x, tb.y + tb.h / 2]; }
      else if (c.side === 'right') { bx = tb.x + tb.w + d; by = tb.y + tb.h / 2 - H / 2; p1 = [bx, by + H / 2]; p2 = [tb.x + tb.w, tb.y + tb.h / 2]; }
      else { bx = tb.x + tb.w / 2 - W / 2; by = tb.y + tb.h + d; p1 = [tb.x + tb.w / 2, by]; p2 = [tb.x + tb.w / 2, tb.y + tb.h]; }
      // optional shift of the label (and arrow start) by dx/dy; ax/ay shift the arrow tip
      if (c.dx || c.dy) { bx += c.dx || 0; by += c.dy || 0; p1 = [p1[0] + (c.dx || 0), p1[1] + (c.dy || 0)]; }
      if (c.ax || c.ay) { p2 = [p2[0] + (c.ax || 0), p2[1] + (c.ay || 0)]; }
      if (c.straight) { if (c.side === 'left' || c.side === 'right') p2[1] = p1[1]; else p2[0] = p1[0]; }
      shapes.push({ t: 'arrow', pts: [p1, p2], color: BLUE, width: 2.5 });
      shapes.push({ t: 'label', x: bx, y: by, w: W, h: H, text: String(c.label), color: BLUE });
      extents.push({ x: bx, y: by, w: W, h: H });
    }
  }
  await page.evaluate((shapes) => {
    const NS = 'http://www.w3.org/2000/svg';
    const doc = document.documentElement;
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('width', doc.scrollWidth); svg.setAttribute('height', doc.scrollHeight);
    svg.style.cssText = 'position:absolute;left:0;top:0;pointer-events:none;z-index:2147483647';
    const defs = document.createElementNS(NS, 'defs'); svg.appendChild(defs);
    const markers = {};
    const marker = (color) => {
      if (markers[color]) return markers[color];
      const id = 'ah' + Object.keys(markers).length;
      const m = document.createElementNS(NS, 'marker');
      m.setAttribute('id', id); m.setAttribute('markerWidth', '5'); m.setAttribute('markerHeight', '5');
      m.setAttribute('refX', '4'); m.setAttribute('refY', '2.5'); m.setAttribute('orient', 'auto'); m.setAttribute('markerUnits', 'strokeWidth');
      const p = document.createElementNS(NS, 'path'); p.setAttribute('d', 'M0,0 L5,2.5 L0,5 z'); p.setAttribute('fill', color);
      m.appendChild(p); defs.appendChild(m); markers[color] = id; return id;
    };
    for (const s of shapes) {
      if (s.t === 'rect') {
        const r = document.createElementNS(NS, 'rect');
        Object.entries({ x: s.x, y: s.y, width: s.w, height: s.h, fill: 'none', stroke: s.color, 'stroke-width': s.width || 4 }).forEach(([k, v]) => r.setAttribute(k, v));
        svg.appendChild(r);
      } else if (s.t === 'arrow') {
        const pl = document.createElementNS(NS, 'polyline');
        pl.setAttribute('points', s.pts.map(p => p.join(',')).join(' '));
        pl.setAttribute('fill', 'none'); pl.setAttribute('stroke', s.color); pl.setAttribute('stroke-width', s.width || 4);
        pl.setAttribute('marker-end', `url(#${marker(s.color)})`);
        svg.appendChild(pl);
      } else if (s.t === 'label') {
        const r = document.createElementNS(NS, 'rect');
        Object.entries({ x: s.x, y: s.y, width: s.w, height: s.h, fill: '#fff', stroke: s.color, 'stroke-width': 2.5 }).forEach(([k, v]) => r.setAttribute(k, v));
        const tx = document.createElementNS(NS, 'text');
        Object.entries({ x: s.x + s.w / 2, y: s.y + s.h / 2 + 7, 'text-anchor': 'middle', 'font-size': 20, 'font-family': 'Arial, sans-serif', fill: '#000' }).forEach(([k, v]) => tx.setAttribute(k, v));
        tx.textContent = s.text; svg.appendChild(r); svg.appendChild(tx);
      }
    }
    doc.appendChild(svg);
  }, shapes);
  return extents;
}

async function cropRect(page, crop, extents) {
  const around = await Promise.all((crop.around || []).map(sel => bbox(page, sel)));
  return union(around.concat(extents), crop.pad ?? 20);
}

module.exports = { annotate, cropRect };
