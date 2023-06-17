from flask import Flask

app = Flask(__name__)
app.secret_key = 'xoxo'

from app import routes
