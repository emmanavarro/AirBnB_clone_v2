#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ List all the states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_states():
    """ List all the cities in a state """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


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
    return render_template('9-states.html', states=states, flag=flag)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ List the states and its cities dynamically """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display home page dynamically """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_db(db):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
