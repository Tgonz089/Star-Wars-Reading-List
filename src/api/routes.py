"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/person', methods=['GET'])
def get_person_all():

    people = Person.query.all()

    return jsonify(characters=[i.serialize() for i in people]), 200


@api.route('/person/<int:person_id>', methods=['GET'])
def get_single_person():

    response_body = {
        "message": "Hello! This will choose a single person"
    }

    return jsonify(response_body), 200


@api.route('/planet/<int:planet_id>', methods=['GET'])
def single_planet():

    response_body = {
        "message": "Hello! This will grab a single planet"
    }

    return jsonify(response_body), 200


@api.route('/planet', methods=['GET'])
def planet_all():

    response_body = {
        "message": "Hello! This will grab all the planets"
    }

    return jsonify(response_body), 200


@api.route('/user/<int:user_id>', methods=['GET'])
def single_user():

    response_body = {
        "message": "Hello! This will grab a single user"
    }

    return jsonify(response_body), 200


@api.route('/user', methods=['GET'])
def user_all():

    response_body = {
        "message": "Hello! This will grab all the users"
    }

    return jsonify(response_body), 200


@api.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def single_vehicle():

    response_body = {
        "message": "Hello! This will grab a single vehicle"
    }

    return jsonify(response_body), 200


@api.route('/vehicle', methods=['GET'])
def vehicle_all():

    response_body = {
        "message": "Hello! This will grab all the users"
    }

    return jsonify(response_body), 200
