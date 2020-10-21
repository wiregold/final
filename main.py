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
                  Language: <input type="text" name="plainText"><br>
                  Framework: <input type="text" name="shift"><br>
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

"""
def decrpyt():
    encryption = input("Enter in your encrypted code")

    n = int(input("enter in your encryption shift"))
    encryption_shift = n * -1
    cipherText1 = ""
    cipherText1 = caesar(encryption, encryption_shift)
    print("Your ciphertext is: ", cipherText1, "with a  negative shift of", encryption_shift)


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def helloword():
    print("Hello World!")


from tkinter import *

menu = Tk()
menu.title("menu")
menu.geometry("300x300")

button0 = Button(menu, text="Hello World", command=helloword)
button0.pack()

button1 = Button(menu, text="Encrypt", command=encrypt)
button1.pack()

button2 = Button(menu, text="Decrypt", command=decrpyt)
button2.pack()

button3 = Button(menu, text="Exit", command=exit)
button3.pack()

menu.mainloop()
"""
