import string
import random
from flask import Flask, request, redirect
app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello, World!'
