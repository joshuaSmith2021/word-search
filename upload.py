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

# next, read the text on the image using google's text recognition
# then delete the image from storage
# then format the recognition response into the proper format for the solver
# prompt user that the formatting looks correct
# * if it is incorrect, ask the user which lines they would like to remove
#   or allow them to modify the data
# once the data is ready, solve the puzzle and output the solution as well as
#     informing the user of any words that were not found
# Once a prototype is working, rewrite the code as reusable functions and put
#     some things into if name == main so the file can still be ran
