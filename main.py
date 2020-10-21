import string
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

""""
def encrypt():
    plainText = input("What is your Plaintext?")
    shift = int(input("What is your shift?"))
    cipherText = caesar(plainText, shift)
    print("Your ciphertext is: ", cipherText, "with a shift of", shift)


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