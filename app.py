from send import send_mail
from blowfish import create_decrypted
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/decrypt',methods=['GET'])
def decrypt_index():
    return render_template('decrypt.html')

@app.route('/', methods=['POST'])
def mail():
    to = request.form['to']
    subject = request.form['subject']
    body = request.form['body']
    send_mail(to,subject,body)
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    enc_text = request.form['decrypt']
    dec_text = create_decrypted(enc_text)
    return render_template('decrypt.html',dec_text = dec_text)

if __name__ == '__main__':
    app.debug = True
    app.run()