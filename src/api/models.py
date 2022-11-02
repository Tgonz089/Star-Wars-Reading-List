from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


user_to_planet = db.Table(
    "user_to_planet",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("User.id")),
    db.Column("planet_id", db.Integer, db.ForeignKey("Planet.id"))
)

user_to_person = db.Table(

    "user_to_person",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("User.id")),
    db.Column("person_id", db.Integer, db.ForeignKey("Person.id"))
)

user_to_vehicle = db.Table(
    "user_to_vehicle",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("User.id")),
    db.Column("vehicle_id", db.Integer, db.ForeignKey("Vehicle.id"))
)

class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256))
    password = db.Column(db.String(256), nullable=False)
    favorite_planet = db.relationship("Planet",
                                 secondary=user_to_planet,
                                 backref=db.backref("users_planet", uselist=True))
    favorite_person = db.relationship("Person",
                                 secondary=user_to_person,
                                 backref=db.backref("users_people", uselist=True))
    favorite_vehicle = db.relationship("Vehicle",
                                 secondary=user_to_vehicle,
                                 backref=db.backref("users_vehicle", uselist=True))
    

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "favorite_planet": [planet.serialize() for planet in self.favorite_planet],
            "favorite_person": [person.serialize() for person in self.favorite_person],
            "favorite_vehicle": [vehicle.serialize() for vehicle in self.favorite_vehicle]
            # do not serialize the password, its a security breach
        }

    def deserialize(data={}):
        return User(**data)


class Person(db.Model):
    __tablename__ = 'Person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    eye_color = db.Column(db.String(25))
    hair_color = db.Column(db.String(25))
    gender = db.Column(db.String(25))
    height = db.Column(db.Float)
    mass = db.Column(db.Float)
    Planet_id = db.Column(db.Integer, db.ForeignKey("Planet.id"))

    def serialize(self):
        return {

            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            # do not serialize the password, its a security breach
        }

    def deserialize(data={}):
        return Person(**data)


class Planet(db.Model):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(256))
    population = db.Column(db.String(256))
    terrain = db.Column(db.String(25))
    gravity = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)

    def serialize(self):
        return {

            "id": self.id,
            "planet_name": self.planet_name,
            "population": self.population,
            "terrain": self.terrain,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            # do not serialize the password, its a security breach
        }

    def deserialize(data={}):
        return Planet(**data)


class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(256))
    crew_size = db.Column(db.String(25))
    model = db.Column(db.String(256))
    cost_in_credits = db.Column(db.Float)
    consumables = db.Column(db.String(256))
    cargo_capacity = db.Column(db.Integer)
    length = db.Column(db.Float)
    manufacturer = db.Column(db.String(256))
    max_atmosphering_speed = db.Column(db.Integer)

    def serialize(self):
        return {

            "id": self.id,
            "vehicle_name": self.vehicle_name,
            "crew_size": self.crew_size,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
            "consumables": self.consumables,
            "cargo_capacity": self.cargo_capacity,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            # do not serialize the password, its a security breach
        }

    def deserialize(data={}):
        return Vehicle(**data)
