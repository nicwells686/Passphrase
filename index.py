#!/usr/bin/env python2
import wordlist_passphrase_generator as w
from flask import Flask
app=Flask(__name__)
@app.route("/")
def Hello_World():
    passw = w.get_passphrase(3)
    return passw
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)