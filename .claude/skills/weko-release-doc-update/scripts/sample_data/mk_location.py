from invenio_app.factory import create_app
app = create_app()
with app.app_context():
    from invenio_db import db
    from invenio_files_rest.models import Location
    loc = Location(name='screenshot-sample-s3', uri='s3://screenshot-sample/', default=False, type='s3',
                   s3_send_file_directly=True, s3_default_block_size=5242880,
                   s3_maximum_number_of_parts=10000, s3_signature_version='s3v4', s3_url_expiration=60)
    db.session.add(loc); db.session.commit()
    print('LOCATION_ID', loc.id)
