from flask import render_template, request, redirect, session
from app import app
from myfirebase import auth

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
    # Login logic here
    return render_template('login.html')

@app.route('/profile')
def profile():
    # Profile logic here
    pass

@app.route('/logout')
def logout():
    # Logout logic here
    pass
