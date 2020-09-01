#!/usr/bin/python3
""" script that starts a Flask web application
    - The web application must be listening on 0.0.0.0, port 5000
    - Routes:
        - /: display "Hello HBNB!"
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ Displays C followed by 'text' variable """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ Displays route in Python """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number_route(n):
    """ Displays a number (int) """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """ Dispays number template """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
