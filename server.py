from flask import Flask, render_template
from jinja2 import StrictUndefined
import os
from service import *

key = os.environ['FLASK_SECRET']

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Homepage, welcoming Hacktober."""
    return render_template('homepage.html')

@app.route('/fortunes')
def show_random_fortune():
    """Shows randomly selected fortune from service."""

    fortune = random_fortune()

    return render_template('fortunes.html',
                            fortune=fortune)


###################
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')