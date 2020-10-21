import string
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
        elif request.form['submit_button'] == 'Substitution Cipher':
            return redirect("https://helloworld4415232.herokuapp.com/substitution")


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
                  <input type="submit" name= "submit_button" value="Substitution Cipher"><br>

              </form>'''


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)




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
