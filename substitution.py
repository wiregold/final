import random
import string
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/substitution', methods=['GET', 'POST'])


alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

def makeKey(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)


key = makeKey(alphabet)
plaintext = "Hey, this is really fun!"


# v! zmhvxdmxdmo!nll mikbg


def encrypt(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)


def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)


cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(key)
print(decrypt(cipher, key, alphabet))
