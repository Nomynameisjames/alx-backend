#!/usr/bin/env python3
from flask import Flask, render_template

"""
    creating a flask app instance
"""

app = Flask(__name__)

@app.route('/')
def index():
    '''flask route index.html'''
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
