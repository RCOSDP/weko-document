// Render markdown with kramed (the engine of honkit): JSON array of strings on stdin -> JSON array of HTML. Used by fix_inline.py.
const kramed = require(process.cwd() + '/docs/node_modules/kramed');
let d=''; process.stdin.on('data',c=>d+=c).on('end',()=>{
  const a=JSON.parse(d); process.stdout.write(JSON.stringify(a.map(s=>{try{return kramed(s)}catch(e){return ''}})));
});
