from importlib import import_module
import os
from flask import Flask, redirect, url_for, session, render_template, Response
from authlib.integrations.flask_client import OAuth
from auth_decorator import login_required
from camera_opencv import Camera
import cv2


def start_ngrok():
    from pyngrok import ngrok

    url = '238ffab4d980.ngrok.io'
    print(' * Tunnel URL:', url)

app = Flask(__name__)

app.secret_key = 'random secret'
oauth = OAuth(app)
video = cv2.VideoCapture('238ffab4d980.ngrok.io/video_feed')

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
