import string
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def encrypt_example():
    if request.method == 'POST':
        plainText = request.form.get('plainText')
        shift = request.form['Shift']
        cipherText = caesar(plainText, shift)
        return '''<h1>ur ciphertext is{}</h1>'''.format(cipherText)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def encrypt():
    plainText = input("What is your Plaintext?")
    shift = int(input("What is your shift?"))
    cipherText = caesar(plainText, shift)
    print("Your ciphertext is: ", cipherText, "with a shift of", shift)
