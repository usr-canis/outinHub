import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase app
cred = credentials.Certificate('app/firebase.json')
firebase_admin.initialize_app(cred)

# Firebase authentication
def create_user(email, password, display_name):
    user = auth.create_user(
        email=email,
        password=password,
        display_name=display_name
    )
    return user
