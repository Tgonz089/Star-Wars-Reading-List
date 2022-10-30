"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/user', methods=['GET'])
def user_all():
    users = User.query.all()

    return jsonify(all_users=[i.serialize() for i in users]), 200


@api.route('/user/<int:user_id>', methods=['GET'])
def single_user(user_id):

    user = User.query.filter_by(id=user_id).all()
    return jsonify(
        all_users=[i.serialize() for i in user]
    )


@api.route('/person', methods=['GET'])
def get_person_all():

    people = Person.query.all()

    return jsonify(characters=[i.serialize() for i in people]), 200


@api.route('/person/<int:person_id>', methods=['GET'])
def get_single_person(person_id):

    single_person = Person.query.filter_by(id=person_id).all()
    return jsonify(
        characters=[i.serialize() for i in single_person]
    ), 200

    return jsonify(response_body), 200


@api.route('/planet', methods=['GET'])
def planet_all():

    planets = Planet.query.all()

    return jsonify(all_planets=[i.serialize() for i in planets]), 200


@api.route('/planet/<int:planet_id>', methods=['GET'])
def single_planet():

    single_planet = User.query.filter_by(id=planet_id).all()

    return jsonify(
        all_planets=[i.serialize() for i in single_planet]
    )
