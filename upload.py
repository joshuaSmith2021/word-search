import firebase_admin as admin
from firebase_admin import storage

def initialize_app(creds):
    cred = admin.credentials.Certificate(creds)
    app = admin.initialize_app(cred, {
        'storageBucket': 'lynx-197900.appspot.com'
    })
    return app


def upload(app, path, file):
    pretty_file = file.split('/')[-1]
    bucket = storage.bucket()
    blob = bucket.blob(path + pretty_file)
    blob.upload_from_filename(file)
    # blob.delete() deletes the file
    return blob


# Once a prototype is working, rewrite the code as reusable functions and put
#     some things into if name == main so the file can still be ran

if __name__ == '__main__':
    credentials_file = 'admin_creds.json'
    app = initialize_app(credentials_file)
    blob = upload(app, 'images/', '../Downloads/library.xml')
    # next, read the text on the image using google's text recognition
    # then delete the image from storage
    # then format the recognition response into the proper format for the solver
    # prompt user that the formatting looks correct
    # * if it is incorrect, ask the user which lines they would like to remove
    #   or allow them to modify the data
    # once the data is ready, solve the puzzle and output the solution as well as
    #     informing the user of any words that were not found
