
from flask.ext.babel import gettext, ngettext
from flask.ext.babel import Babel

#gettext(u'A simple string')
#gettext(u'Value: %(value)s', value=42)
#ngettext(u'%(num)s Apple', u'%(num)s Apples', number_of_apples)

from flask import Flask, g, request, render_template
app = Flask(__name__)

app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)


@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['en','zh'])

@app.route("/")
def hello():
    return render_template( "index.html", content = gettext( "Hello World!" ) )

if __name__ == "__main__":
    app.run( debug = True, host = "0.0.0.0" )

