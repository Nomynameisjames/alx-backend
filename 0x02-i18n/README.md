				 i18n(Internationalize)

Flask-Babel is a Python library that helps you internationalize and localize your Flask web application.
It uses the industry standard i18n and l10n formats to allow you to display your web app in multiple languages and formats.

	Installation

You can install Flask-Babel using pip:
```pip install Flask-Babel```

	Configuration

To configure Flask-Babel, you need to do the following:

1. Import the Babel class from Flask-Babel.

```from flask_babel import Babel```

2. Create an instance of the Babel class.

```babel = Babel(app)```

3. Set the LANGUAGES configuration variable to a list of supported languages. For example:

```app.config['LANGUAGES'] = ['en', 'es', 'fr']```

4. Set the BABEL_DEFAULT_LOCALE configuration variable to the default language. For example:

```app.config['BABEL_DEFAULT_LOCALE'] = 'en'```

Usage

To use Flask-Babel, you need to do the following:

1. Create translation files for each language you want to support.
You can use the pybabel command-line tool to generate translation files from your source code. For example:

```pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -D messages -D errors -D forms -D navigation```

2. Add the gettext function to your templates. For example:
	```{% trans "Hello, World!" %}```

3. Use the gettext function in your Python code. For example:

	```from flask_babel import gettext

		@app.route('/')
		def hello():
    			return gettext('Hello, World!')```

4. Add a language switcher to your templates. For example:
	
	```{% for lang in get_languages() %}
  		<a href="{{ set_locale(lang) }}">{{ lang }}</a>
	   {% endfor %}```



