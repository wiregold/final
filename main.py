import string
import random
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'