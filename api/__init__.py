import os

from flask import Flask, jsonify

from flask_sqlalchemy import SQLAlchemy


"""Crate the application instance"""

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)


@app.route('/api/v1/', methods=["GET"])
def get_welcome():
    return jsonify({"message": "Welcome to appointments"})


# initialize the database as we create the app
database.init_app(app)


from api.views.doctors import doctors
from api.views.patients import patients
from api.views.appointments import appointments
from api.views.slots import slots

