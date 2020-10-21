import string
import random
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def encrypt_example():
    if request.method == 'POST':
        if request.form['submit_button'] == 'SubmitEncrypt':
            plainText = request.form.get('plainText')
            var1 = request.form.get('var1')
            shift = int(var1)
            cipherText = caesar(plainText, shift)
            return '''<h1>The plainText value is: {}</h1>
                          <h1>The shift value is: {}</h1>'''.format(cipherText, shift)

        elif request.form['submit_button'] == 'SubmitDecrypt':
            plainText1 = request.form.get('plainText1')
            var2 = request.form.get('var2')
            var3 = int(var2)
            shift1 = var3 * -1
            cipherText1 = caesar(plainText1, shift1)
            return '''<h1>The Unencrypted value is: {}</h1>
                                      <h1>The shift value is: {}</h1>'''.format(cipherText1, shift1)

        elif request.form['submit_button'] == 'Submit Substitution':

            alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

            def makeKey(alphabet):
                alphabet = list(alphabet)
                random.shuffle(alphabet)
                return ''.join(alphabet)

            key = makeKey(alphabet)
            subtext1 = request.form.get('subtext1')

            def encrypt(plaintext, key, alphabet):
                keyIndices = [alphabet.index(k.lower()) for k in plaintext]
                return ''.join(key[keyIndex] for keyIndex in keyIndices)

            cipher = encrypt(subtext1, key, alphabet)

            return '''<h1>The Unencrypted value is: {}</h1>
                      <h1>The Key is: {}</h1>
                       <h1>The Encrypted Text is: {}</h1>'''.format(subtext1, key, cipher)

        elif request.form['submit_button'] == 'Submit Substitution Decrypt':
            cipher2 = request.form.get('subtext2')
            alphabet2 = 'abcdefghijklmnopqrstuvwxyz.,! '
            key2 = request.form.get('key2')

            def decrypt(cipher2, key2, alphabet2):

                key2Indices = [key2.index(k) for k in cipher2]
                return ''.join(alphabet2[key2Index] for key2Index in key2Indices)

            sub2 = decrypt(cipher2, key2, alphabet2)
            return '''<h1>The Unencrypted value is: {}</h1>'''.format(sub2)

    return '''<form method="POST">
                  
                  <h1>Caesar Encryption</h1>  
                  Insert Plaintext: <input type="text" name="plainText"><br>
                  Insert Shift Value: <input type="text" name="var1"><br>
                  <input type="submit" name= "submit_button" value="SubmitEncrypt"><br>
                  <br><br><br>
                  
                  <h1>Caesar Decryption</h1>  
                  Insert Encrypted Text: <input type="text" name="plainText1"><br>
                  Insert Shift Value: <input type="text" name="var2"><br>
                  <input type="submit" name= "submit_button" value="SubmitDecrypt"><br>
                  <br><br><br>
                  
                  
                  <h1>Substitution Encryption</h1>  
                  Insert Plaintext: <input type="text" name="subtext1"><br>
                  <input type="submit" name= "submit_button" value="Submit Substitution"><br>
                  <br><br><br>
                  
                  <h1>Substitution Decryption</h1>  
                  Insert Encrypted Text: <input type="text" name="subtext2"><br>
                  Insert Key: <input type="text" name="key2"><br>
                  <input type="submit" name= "submit_button" value="Submit Substitution Decrypt"><br>
                  <br><br><br>

              </form>'''


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
