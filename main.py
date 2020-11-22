import string
import random
from flask import Flask, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'random secret'
oauth = OAuth(app)


# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='303773199618-f4b58nlg6migc21qii5pqm2m3av07qro.apps.googleusercontent.com',
    client_secret='IrRzNZI1Fr3Y3xSDrjG5_zaZ',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)


from auth_decorator import login_required

@app.route('/')
def start():
    return f'Please redirect to /login to begin'


@app.route('/main')
@login_required
def hello_world():
    email = dict(session).get('email', None)
    return f'Hello, {email}!'


@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    session['logged_in'] = True
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['email'] = user_info['email']
    # do something with the token and profile
    return redirect('/main')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/main')
