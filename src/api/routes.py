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


@api.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def single_vehicle(vehicle_id):

    single_vehicle = Vehicle.query.filter_by(id=vehicle_id).all()

    return jsonify(
        all_vehicles=[i.serialize() for i in single_vehicle]
    )


@api.route('/users/favorites', methods=['GET'])
def get_fav_planet():
    users = User.query.all()
    for user in users:
        for planet in user.favorite_planet:
            result = planet.planet_name
        for person in user.favorite_person:
            per_result = person.name
        for vehicle in user.favorite_vehicle:
            veh_result = vehicle.vehicle_name
    return jsonify(result, per_result, veh_result)


@api.route("/planet/<int:planet_id>", methods=["POST"])
def add_planet(planet_id):
    new = request.get_json()
    new_planet = Planet(id=planet_id, planet_name=new["planet_name"])
    db.session.add(new_planet)
    db.session.commit()

    return jsonify("A Planet was added"), 200


@api.route("/person/<int:person_id>", methods=["POST"])
def add_person(person_id):
    new = request.get_json()
    new_person = Person(id=person_id, name=new["name"])
    db.session.add(new_person)
    db.session.commit()

    return jsonify("A Person was added."), 200


@api.route("/vehicle/<int:vehicle_id>", methods=["POST"])
def add_vehicle(vehicle_id):
    new = request.get_json()
    new_vehicle = Vehicle(id=vehicle_id, vehicle_name=new["vehicle_name"])
    db.session.add(new_vehicle)
    db.session.commit()

    return jsonify("A Vehicle was added."), 200


@api.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    deleted_vehicle = Vehicle.query.get(vehicle_id)
    if deleted_vehicle == None:
        return ("This vehicle does not exist."), 200
    else:
        db.session.delete(deleted_vehicle)
        db.session.commit()   
        return jsonify("Vehicle was deleted."),200

@api.route('/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    deleted_person = Person.query.get(person_id)
    if deleted_person == None:
        return ("This person does not exist."), 200
    else:
        db.session.delete(deleted_person)
        db.session.commit()   
        return jsonify("Person was deleted."),200


@api.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    deleted_planet = Planet.query.get(planet_id)
    if deleted_planet == None:
        return ("This planet does not exist."), 200
    else:
        db.session.delete(deleted_planet)
        db.session.commit()   
        return jsonify("Planet was deleted."),200