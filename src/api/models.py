from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256))
    password = db.Column(db.String(256), nullable=False)
    Planet_To_Favorites_id = db.Column(
        db.Integer, db.ForeignKey("Planet_To_Favorites.id"))
    Person_To_Favorites_id = db.Column(
        db.Integer, db.ForeignKey("Person_To_Favorites.id"))
    Vehicle_To_Favorites_id = db.Column(
        db.Integer, db.ForeignKey("Vehicle_To_Favorites.id"))

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def deserialize(data={}):
        return User(**data)


class Person(db.Model):
    __tablename__ = 'Person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    person_fav_id = db.Column(db.Integer)
    name = db.Column(db.String(256))
    eye_color = db.Column(db.String(25))
    hair_color = db.Column(db.String(25))
    gender = db.Column(db.String(25))
    height = db.Column(db.Float)
    mass = db.Column(db.Float)
    Planet_id = db.Column(db.Integer, db.ForeignKey("Planet.id"))
    person = db.relationship("Person_To_Favorites")

    def serialize(self):
        return {

            "id": self.id,
            "person_fav_id": self.person_fav_id,
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
    planet_fav_id = db.Column(db.Integer)
    planet_name = db.Column(db.String(256))
    population = db.Column(db.String(256))
    terrain = db.Column(db.String(25))
    gravity = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    planet = db.relationship("Planet_To_Favorites")

    def serialize(self):
        return {

            "id": self.id,
            "planet_fav_id": self.planet_fav_id,
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
    vehicle = db.relationship("Vehicle_To_Favorites")

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


class Person_To_Favorites(db.Model):
    __tablename__ = 'Person_To_Favorites'
    person_id = db.Column(db.Integer, db.ForeignKey(
        "Person.id"), primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)


class Planet_To_Favorites(db.Model):
    __tablename__ = 'Planet_To_Favorites'
    planet_id = db.Column(db.Integer, db.ForeignKey(
        "Planet.id"), primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)


class Vehicle_To_Favorites(db.Model):
    __tablename__ = 'Vehicle_To_Favorites'
    vehicle_id = db.Column(db.Integer, db.ForeignKey(
        "Vehicle.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)
