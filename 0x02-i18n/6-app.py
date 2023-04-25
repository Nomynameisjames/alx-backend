#!/usr/bin/env python3
"""import files """
from flask import Flask, render_template, request, g
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

"""
    users  mock a database user table.
"""
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
        function returns a user dictionary or None
        if the ID cannot be found or if login_as was not passed.
    """
    ID = request.args.get('login_as', None)
    if ID is not None and int(ID) in users.keys():
        return users.get(int(ID))
    return None


@app.before_request
def before_request():
    """
        find a user if any, and set it as a global on flask.g.user.
    """
    User = get_user()
    g.user = User


@babel.localeselector
def get_locale():
    """
        return best language match based on supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''flask route index.html'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
