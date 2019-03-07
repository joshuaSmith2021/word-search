import firebase_admin as admin
from firebase_admin import storage

source_file = '../Downloads/library.xml'

cred = admin.credentials.Certificate('admin_creds.json')
app = admin.initialize_app(cred, {
    'storageBucket': 'lynx-197900.appspot.com'
})

bucket = storage.bucket()
blob = bucket.blob('images/{}'.format(source_file.split('/')[-1]))
blob.upload_from_filename(source_file)
print('File {} uploaded to {}'.format(source_file, 'images/'))
