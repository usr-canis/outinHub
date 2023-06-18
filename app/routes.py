import firebase_admin
from flask import Flask, render_template, redirect, url_for, request, flash,session
from app import app
from myfirebase import create_user,sign_in_with_email_and_password
from myfirebase import auth
import requests

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

    return render_template('login.html')

@app.route('/profile')
def profile():
    # Profile logic here
    pass

@app.route('/logout')
def logout():
    # Logout logic here
    pass
