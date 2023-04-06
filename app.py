from flask import Flask, request
from markupsafe import escape
from art import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ascii art generator'

@app.route('/art/<word>/<decoration>')
def art_generator(word, decoration):
    data = request.get_data().decode('utf-8')
    Art = text2art(word, decoration)
    return '<pre>' + Art + '<pre>'

if __name__ == '__main__':
    app.debug = True
    app.run()
