#!/usr/bin/env python3
"""import files """
from flask import Flask, render_template, request
from flask_babel import Babel
import os


class Config(object):
    """
        Babel   Configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""
    creating a flask app instance
"""

app = Flask(__name__)
app.config.from_object(Config)
""" creating an instance of the Babel class"""
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
        return best language match based on supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''flask route index.html'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
