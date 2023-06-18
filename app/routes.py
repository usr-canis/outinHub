import firebase_admin
from flask import Flask, render_template, redirect, url_for, request, flash,session
from app import app
from myfirebase import create_user
from myfirebase import auth
import mypyrebase
from mypyrebase import auth

FIREBASE_AUTH_URL = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/"


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username
            )
            # User created successfully, redirect to the login page
            return redirect('/login')

        except auth.EmailAlreadyExistsError:
            error = 'Email address already exists.'
            return render_template('signup.html', error=error)

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(
                email=email,
                password=password,)
            print(user)
            session['user_token'] = user['idToken']
            session['user_id'] = user['localId']
            session['email'] = user['email']
            session['username']=user['displayName']
            return redirect('/dashboard')

        except:
            error = 'Invalid login credentials'
            return render_template('login.html', error=error)


     return render_template('login.html')

@app.route('/dashboard')
def dashboard():
     if 'user_token' in session:
        # User is logged in, render the dashboard template
        username = session['username']
        return render_template('dash.html', username=username)
     else:
        # User is not logged in, redirect to the login page
        return redirect('/login')   
