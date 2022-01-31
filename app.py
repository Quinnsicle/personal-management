from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hi(name=None):
    return render_template('hi.html', name=name)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)