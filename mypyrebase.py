import pyrebase

config = {
  "apiKey": "AIzaSyBuuRhx_2litCWmf6ed-CJdMYYwLcTrlko",
  "authDomain": "outinhub.firebaseapp.com",
  "databaseURL": "https://outinhub-default-rtdb.firebaseio.com",
  "projectId": "outinhub",
  "storageBucket": "outinhub.appspot.com",
  "messagingSenderId": "1053181631064",
  "appId": "1:1053181631064:web:daa41b9f779ff70aa8482d",
  "measurementId": "G-XZPBHTV8HV"
}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

db = firebase.database()
db.child("users").child("Morty")
    
