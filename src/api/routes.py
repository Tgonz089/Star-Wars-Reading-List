"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Person, Planet, Vehicle
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# This will get all users.


@api.route('/user', methods=['GET'])
def user_all():
    users = User.query.all()

    return jsonify(all_users=[i.serialize() for i in users]), 200

# This will get a single user.


@api.route('/user/<int:user_id>', methods=['GET'])
def single_user(user_id):

    user = User.query.filter_by(id=user_id).all()
    return jsonify(
        single_user=[i.serialize() for i in user]
    )

# This will get all charcters.


@api.route('/person', methods=['GET'])
def get_person_all():

    people = Person.query.all()

    return jsonify(all_characters=[i.serialize() for i in people]), 200

# This will get a single charcter.


@api.route('/person/<int:person_id>', methods=['GET'])
def get_single_person(person_id):

    single_person = Person.query.filter_by(id=person_id).all()
    return jsonify(
        single_character=[i.serialize() for i in single_person]
    ), 200

# This will get all planets.


@api.route('/planet', methods=['GET'])
def planet_all():

    planets = Planet.query.all()

    return jsonify(all_planets=[i.serialize() for i in planets]), 200

# This will get a single planet.


@api.route('/planet/<int:planet_id>', methods=['GET'])
def single_planet(planet_id):

    single_planet = Planet.query.filter_by(id=planet_id).all()

    return jsonify(
        planet=[i.serialize() for i in single_planet]
    )

# This will get all vehicles.


@api.route('/vehicle', methods=['GET'])
def vehicle_all():

    vehicles = Vehicle.query.all()

    return jsonify(all_vehicles=[i.serialize() for i in vehicles]), 200

# This will get a single vehicle.


@api.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def single_vehicle(vehicle_id):

    single_vehicle = Vehicle.query.filter_by(id=vehicle_id).all()

    return jsonify(
        single_vehicle=[i.serialize() for i in single_vehicle]
    )

# This will list all the user's favorite, planets, characters, and vehicles.


@api.route('/user/favorites', methods=['GET'])
def get_favorite():
    users = User.query.all()
    for user in users:
        single_user = user.name
        for planet in user.favorite_planet:
            planet_result = planet.planet_name
        for person in user.favorite_person:
            person_result = person.name
        for vehicle in user.favorite_vehicle:
            vehicle_result = vehicle.vehicle_name

    return jsonify(single_user,
                   "Favorite planet is " + planet_result,
                   "Favorite character is " + person_result,
                   "Favorite vehicle is the " + vehicle_result,
                   )

# This will list a specific user's favorite planets, characters, and vehicles.


@api.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_favorites(user_id):
    users = User.query.filter_by(id=user_id).all()
    for user in users:
        for planet in user.favorite_planet:
            planet_result = planet.planet_name
        for person in user.favorite_person:
            person_result = person.name
        for vehicle in user.favorite_vehicle:
            vehicle_result = vehicle.vehicle_name
    return jsonify(user.name,
                   "Favorite planet is " + planet_result,
                   "Favorite character is " + person_result,
                   "Favorite vehicle is the " + vehicle_result)


@api.route("/user/<int:user_id>/favorites", methods=["POST"])
def add_planet_user(user_id):
    new = request.get_json()
    new_planet = Planet(id=planet_id, planet_name=new["planet_name"])
    db.session.add(new_planet)
    db.session.commit()

    return jsonify("A Planet was added to the user's favorites."), 200

# This will add a new planet to Planets.


@api.route("/planet/<int:planet_id>", methods=["POST"])
def add_planet(planet_id):
    new = request.get_json()
    new_planet = Planet(id=planet_id, planet_name=new["planet_name"])
    db.session.add(new_planet)
    db.session.commit()

    return jsonify("A Planet was added."), 200

# This will add a new character to Person.


@api.route("/person/<int:person_id>", methods=["POST"])
def add_person(person_id):
    new = request.get_json()
    new_person = Person(id=person_id, name=new["name"])
    db.session.add(new_person)
    db.session.commit()

    return jsonify("A Person was added."), 200

# This will add a new vehicle to Vehicles.


@api.route("/vehicle/<int:vehicle_id>", methods=["POST"])
def add_vehicle(vehicle_id):
    new = request.get_json()
    new_vehicle = Vehicle(id=vehicle_id, vehicle_name=new["vehicle_name"])
    db.session.add(new_vehicle)
    db.session.commit()

    return jsonify("A Vehicle was added."), 200

# This will delete a vehicle with the targeted id.


@api.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    deleted_vehicle = Vehicle.query.get(vehicle_id)
    if deleted_vehicle == None:
        return ("This vehicle does not exist."), 200
    else:
        db.session.delete(deleted_vehicle)
        db.session.commit()
        return jsonify("Vehicle was deleted."), 200

# This will delete a character with the targeted id.


@api.route('/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    deleted_person = Person.query.get(person_id)
    if deleted_person == None:
        return ("This person does not exist."), 200
    else:
        db.session.delete(deleted_person)
        db.session.commit()
        return jsonify("Person was deleted."), 200

# This will delete a planet with the targeted id.


@api.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    deleted_planet = Planet.query.get(planet_id)
    if deleted_planet == None:
        return ("This planet does not exist."), 200
    else:
        db.session.delete(deleted_planet)
        db.session.commit()
        return jsonify("Planet was deleted."), 200


@api.route('/user/<int:user_id>/favorites', methods=['DELETE'])
def delete_fav(user_id):
    users = User.query.filter_by(id=user_id).all()
    for user in users:
        for planet in user.favorite_planet:
            planet_result = planet.planet_name
    return jsonify("Deleted Favorite.")


@api.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("passord", None)
    user = User.query.filter_by(email=email).one_or_none()
    if user is not None:
        if user.check_password_hash(password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token)
    return jsonify({"msg": "Invalid cedentials."}), 401
