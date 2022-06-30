import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def add():
    sum = 0
    x = float(request.form['input1'])
    y = float(request.form['input2'])
    sum = np.sqrt(x)
    return render_template('index.html',sum=sum)

if __name__ == '__main__':
    app.debug = True
    app.run()