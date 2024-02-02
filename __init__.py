from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')

def monfr():
    return "<h2>Bonjour tout le monde !</h2>"
def hello_world():
    return render_template('hello.html')
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
