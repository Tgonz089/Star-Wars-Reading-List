"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Person, Planet, Vehicle
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
def single_planet(planet_id):

    single_planet = User.query.filter_by(id=planet_id).all()

    return jsonify(
        all_planets=[i.serialize() for i in single_planet]
    )

@api.route('/vehicle', methods=['GET'])
def vehicle_all():

    vehicles = Vehicle.query.all()

    return jsonify(all_vehicles=[i.serialize() for i in vehicles]), 200


@api.route('/planet/<int:vehicle_id>', methods=['GET'])
def single_vehicle(vehicle_id):

    single_vehicle = Vehicle.query.filter_by(id=vehicle_id).all()

    return jsonify(
        all_vehicles=[i.serialize() for i in single_vehicle]
    )

@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_vehicle(user_id):
    deleted_vehicle = User.query.get(id=favorite_vehicle)
    if deleted_vehicle == None:
        return ("this vehicle does not exist"),200
    else:
        db.session.delete(deleted_vehicle)
        db.session.commit()   
        return jsonify("Vehicle deleted from the User's favorites."),200

#@api.route("/person/<int:person_id>", methods = ["POST"])
#def add_favorite(person_id):
#    new = request.get_json()
 #   new_favorite = User(user_id=new["user_id"], person_id=new["person_id"])
 #   db.session.add(new_favorite)
   # db.session.commit()

    #return jsonify("Person added to favourites"),200
