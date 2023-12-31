import firebase_admin 
from firebase_admin import credentials, auth,_auth_client
from flask import session  
import firebase   
import os
import requests
import json

FIREBASE_WEB_API_KEY = os.environ.get("AIzaSyBuuRhx_2litCWmf6ed-CJdMYYwLcTrlko")
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

# Initialize Firebase app
cred = credentials.Certificate({ "type": "service_account",
    "project_id": "outinhub",
    "private_key_id": "ae0abef3f146f8056cc49e415427d649dc3b7170",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCVkkTGxMFxBpLj\nzBTTSyQ1eDKjUEZe/ij0eU/K/1HTslkQGDVI0+4lk1I/DsGtQa7zjowLUXDfg4I4\neAV5advRhrvU7gx8v7Tp/pOfHR+0a7tyvCD9F/qK6yTonN/g7MZPn1DLyb6kVh2H\nuj9PSzqrbBjLG/UVzMNJDn26DQGE6FbZgbzoyn1kX9dvFEkUCmNNAubMR7q8VeV6\n5Tef3DGcowdvzCVn4lkzRx0N30s492OQNm3IoR2q0wYsIHvHG06Zn/RCRF4r24C8\niWNhKv5DEVMFGT6Sf2lKm3GQAtCwXHVd12PlbmgHyLsX7y0V9lQrxatuo2tQyINP\naWphAr47AgMBAAECggEAE5iy5yH/QDo+w5bJAbf+Gf1SESCi365IGmPMhwm1pFlh\nHuE1FgIiWQz4wSdDS9pnvCRoh9EXS0mVJaXf/bzXXpfbAzZfL3cEkoXWvImZzk8x\nI4Kvhcl++3V8g/eNw4/yGZuDf/fCQRDBVLebtN1j5fLHOtFCZqVJzsgVw+sRUGLX\nOvGTda9oPNBzQnRtGDhp+VLtKtyvvl0TC85xfoAiXosg4RSMvenq/WgAae+M0d7v\n0wpbp7m9Wpt93Epaqd580NyDKiFGWEaHnJCq71itD7m4yCGc9yGVkulUxA9b2AwB\nCJwjUeuzEbl+O/Ku0Ji4vBaX+MkCX0MHMrANWwkegQKBgQDFtGuaQunreJ/We2ZF\nZmo60FHjE0v8fwuXUFaf3hyk0v65AYr/ihNyPCZAjrMp8YhOPrTaKVmracBw+QD6\npaFQeG9I5GBlNxSpDNas2PK4rMQg+WQS35ZT+KJjAAq/ngfP0+DdkpmZgxKUjvSM\n+F9btnO1AymtR60b/FyxeyemuwKBgQDBrInRRvAPkQE4XU5amOeK5ZS4mNVDwtGa\n5ZExTUZrJuLMoM6ApuK3dirHqJIOqZMjRaoacJA0ofk2O6Dt7mKkgzWlyYlh9d5i\nXUxQ5RpPrqLtFvsJmVfhvd+a6op8v6FmqEOYu2tHjTTsAu/HtylsUnUgboRlbzlL\nKI6Tr+SOgQKBgA0cS85tBYoh86eLg1qy0fSYf/Wo/+78lc4w+62aUxfzDgVCvu73\nPxbiOj8pt2PeqoVVzzRwbYvadXKIcLIubaYidm7FBkdwAaS8PzgzItVwT4lIQISn\n4xYqdMpP5GaUmjwD9vN6l0kA0iib2kfG6LvyO3YTgZ4GFMq4T4VNf3GlAoGAXFo9\nIbk08gdQUKNVoKf3CWmugFQIphY5QyajFKJnqOLTFYa80eZCh/9mKOz+MNW13wTy\nN0djzGVMZAsNE0gwa4hRxauTwk2u7LLWmGCXKlX5RRtHO+2OVYvoG4Qp45CxkzU7\nfpIoducjzEMeOdries/bIErzATeHV4qQamZek4ECgYBAW8n7G8C3f1FnArlxVZyN\nh6HSmaUOpReniVN+HRoCv80kZ8bM4cbPrZJ5e1nvR+d6fssfyOr5t4FTAXKYOncm\nmpCASL8kq1sTmJUDDkGSdLBnImiRNAXOMQgJLGJiYV/m4RROLzJlCPZ8htr9VBFs\ntAwVSvtN9eyzxY2N6yJvEQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-adtkx@outinhub.iam.gserviceaccount.com",
    "client_id": "117634645103510455373",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-adtkx%40outinhub.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"})

firebase_admin.initialize_app(cred)


# Firebase authentication
def create_user(email, password, display_name):
    user = auth.create_user(
        email=email,
        password=password,
        display_name=display_name
    )
    return user
