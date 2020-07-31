# -*- coding: utf-8-*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return '<h1>Hello 恒升指数Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
