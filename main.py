from importlib import import_module
import os
from flask import Flask, redirect, url_for, session, render_template, Response
from authlib.integrations.flask_client import OAuth
from auth_decorator import login_required
from camera_opencv import Camera
import cv2

app = Flask(__name__)


def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass

    # Initialize our ngrok settings into Flask
    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
    )

    # pyngrok will only be installed, and should only ever be initialized, in a dev environment


from pyngrok import ngrok

# Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
# when starting the server
port = 5000

# Open a ngrok tunnel to the dev server
public_url = http://4a604b20d6ac.ngrok.io

# Update any base URLs or webhooks to use the public ngrok URL
app.config["BASE_URL"] = public_url
init_webhooks(public_url)

app.secret_key = 'random secret'
oauth = OAuth(app)
video = cv2.VideoCapture(0)

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


def start_ngrok():
    from pyngrok import ngrok

    url = ngrok.connect(5000)
    print(' * Tunnel URL:', url)


@app.route('/')
def root():
    return render_template('login.html')


def gen(camera):
    while True:
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video')
def vid():
    return render_template('video.html')


@app.route('/login')
def login():
    session['logged_in'] = True
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['email'] = user_info['email']
    # do something with the token and profile
    return redirect('/index')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/index')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
