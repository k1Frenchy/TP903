from flask import Flask
from os import environ
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = {"message":environ.get('MESSAGE')}
    return msg

app.run('0.0.0.0',port=environ.get('APP_PORT'))
