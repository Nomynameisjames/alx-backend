#!/usr/bin/env python3
"""import files """
from flask import Flask, render_template
from flask_babel import Babel
from flask import request
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

"""
    setting up get_locale function with the babel.localeselector decorator.
    Using request.accept_languages to determine the best match
    with our supported languages.
"""
@babel.localeselector
def get_locale():
    '''get_locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])i


@app.route('/')
def index():
    '''flask route index.html'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
