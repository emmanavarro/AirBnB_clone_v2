#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ List all the states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ List all the states by id """
    flag = 0
    states = None
    all_states = storage.all(State).values()
    for state in all_states:
        if id in state.id:
            flag = 1
            states = state
            break
    return render_template('9-states.py', states=states, flag=flag)


@app.teardown_appcontext
def close_db(db):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
