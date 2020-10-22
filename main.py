import string
import random
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def encrypt_caesar():
    if request.method == 'POST':
        if request.form['submit_button'] == 'SubmitEncrypt':
            plainText = request.form.get('plainText')
            var1 = request.form.get('var1')
            shift = int(var1)
            cipherText = caesar(plainText, shift)
            return '''<h1>The plainText value is:{}</h1>
                          <h1>The shift value is:{}</h1>'''.format(cipherText, shift)

        elif request.form['submit_button'] == 'SubmitDecrypt':
            plainText1 = request.form.get('plainText1')
            var2 = request.form.get('var2')
            var3 = int(var2)
            shift1 = var3 * -1
            cipherText1 = caesar(plainText1, shift1)
            return '''<h1>The Unencrypted value is:{}</h1>
                    <h1>The shift value is:{}</h1>'''.format(cipherText1, shift1)

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

            return '''<h1>The Unencrypted value is:{}</h1>
                      <h1>The Key is:{}</h1>
                       <h1>The Encrypted Text is:{}</h1>'''.format(subtext1, key, cipher)

        elif request.form['submit_button'] == 'Submit Substitution Decrypt':
            cipher2 = request.form.get('subtext2')
            alphabet2 = 'abcdefghijklmnopqrstuvwxyz.,! '
            key2 = request.form.get('key2')

            def decrypt(cipher2, key2, alphabet2):

                key2Indices = [key2.index(k) for k in cipher2]
                return ''.join(alphabet2[key2Index] for key2Index in key2Indices)

            sub2 = decrypt(cipher2, key2, alphabet2)
            return '''<h1>The Unencrypted value is:{}</h1>'''.format(sub2)

    return '''
    
    
    <form method="POST">
                  <html>
                  <head>
                  </head>                  
                  <style>
h1   {color: Grey;
        font-family: Verdana}

input[type=text], select {
  width: 40%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 50%;
  background-color: #7173EB;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #2A2DD1;
}
label{
    display: inline-block;
    font-family: Verdana;
    font-size: 17;
    width: 10%;
    text-align: left;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

</style>
                  <body>
                  
                  <h1>Caesar Encryption</h1>  
                  <label for="plainText">Insert Plaintext:</label> <input type="text" name="plainText"><br>
                  <label for="var1">Insert Shift Value:</label> <input type="text" name="var1"><br>
                  <input type="submit" name= "submit_button" value="SubmitEncrypt"><br>
                  <br><br><br>
                  
                  <h1>Caesar Decryption</h1>  
                 <label for="plainText1"> Insert Encrypted Text:</label> <input type="text" name="plainText1"><br>
                  <label for="var2">Insert Shift Value:</label> <input type="text" name="var2"><br>
                  <input type="submit" name= "submit_button" value="SubmitDecrypt"><br>
                  <br><br><br>
                  
                  <hr noshade width=100% align=left>
                  
                  <h1>Substitution Encryption</h1>  
                  <label for="subtext1">Insert Plaintext:</label> <input type="text" name="subtext1"><br>
                  <input type="submit" name= "submit_button" value="Submit Substitution"><br>
                  <br><br><br>
                  
                  <h1>Substitution Decryption</h1>  
                  <label for="subtext2">Insert Encrypted Text:</label> <input type="text" name="subtext2"><br>
                  <label for="key2">Insert Key:</label> <input type="text" name="key2"><br>
                  <input type="submit" name= "submit_button" value="Submit Substitution Decrypt"><br>
                  <br><br><br>
    </body>
              </form>
              </html>
              '''


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
