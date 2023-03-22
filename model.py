from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GuestUser(db.model):

    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    

class RestaurantUser(db.model):

    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    

class GuestReview(db.model):
    """a review of a particular guest made by the restaurant"""

    __tablename__ = "guest_reviews"

class RestaurantReview(db.model):
    """a review of a particular restaurant made by the guest that dined there"""

    __tablename__ = "restaurant_reviews"

class BannedGuest(db.model):
    """an account of a guest that has been banned from a restaurant"""

    __tablename__ = "banned_guests"





    