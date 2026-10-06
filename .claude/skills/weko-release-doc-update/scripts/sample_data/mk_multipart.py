import uuid
from invenio_app.factory import create_app
app = create_app()
with app.test_request_context():
    from flask_login import login_user
    from invenio_accounts.models import User
    from invenio_db import db
    from invenio_files_rest.models import Bucket, FileInstance, MultipartObject
    login_user(User.query.get(6))
    # remove the two empty buckets left by the failed first attempts
    for bid in ('5e16b720-0189-4e1a-83d0-e1f3b9d74cd6', 'b679278f-ebb0-4de0-a252-6932d2ff790f'):
        b = Bucket.query.get(bid)
        if b is not None and b.size == 0 and not b.objects:
            db.session.delete(b)
    db.session.commit()
    b = Bucket.query.get(bid) or None
    b = Bucket.create()
    db.session.commit()
    out = []
    for k in ('screenshot-sample_1.txt', 'screenshot-sample_2.txt'):
        with db.session.begin_nested():
            f = FileInstance.create()
            f.size = 10*1024*1024
            mp = MultipartObject(upload_id=uuid.uuid4(), bucket=b, key=k, chunk_size=5*1024*1024,
                                 size=10*1024*1024, completed=False, file=f)
            b.size += mp.size
            db.session.add(mp)
        db.session.commit()
        out.append((str(mp.upload_id), str(f.id)))
    print('BUCKET', b.id); print('MP', out)
