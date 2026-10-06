import time
from invenio_app.factory import create_app
app = create_app()
with app.test_request_context():
    from flask_login import login_user
    from invenio_accounts.models import User
    from invenio_db import db
    from weko_index_tree.api import Indexes
    from weko_index_tree.models import Index
    login_user(User.query.get(6))
    iid = int(time.time()*1000)
    Indexes.create(0, {"id": iid, "value": "screenshot-sample インデックス"})
    idx = Index.query.get(iid)
    idx.index_name = "screenshot-sample インデックス"
    idx.index_name_english = "screenshot-sample Index"
    idx.public_state = True
    idx.harvest_public_state = True
    db.session.commit()
    print("INDEX_ID", iid, idx.browsing_role, idx.contribute_role)
