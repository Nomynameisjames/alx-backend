#!/usr/bin/env python3
"""import files """
from flask import Flask, render_template
from flask_babel import Babel
import os
"""
    creating a flask app instance
"""

app = Flask(__name__)

""" creating an instance of the Babel class"""
babel = Babel(app)

""" creating a config class """


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    LANGUAGES = ["en", "fr"]

    @staticmethod
    def init_app(app): pass


""" setting a default language with the config class"""
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_LOCALE'] = 'UTC'


@app.route('/')
def index():
    '''flask route index.html'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
