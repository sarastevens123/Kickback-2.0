from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.model):

    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    guest_reviews = db.relationship("GuestReview", back_populates='guest')
    restaurant_reviews= db.relationship("RestaurantReview", back_populates='guest')

    def __repr__(self):
        return f"<Guest:{self.fname},{self.lname}>"


class Restaurant(db.model):

    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    restaurant_reviews = db.relationship("RestaurantReview", back_populates="restaurant")
    guest_reviews = db.relationship("GuestReview", back_populates="restaurant")

    def __repr__(self):
        return f"<Restaurant:{self.name}, Id:{self.id}>"
    
class GuestReview(db.model):
    """a review of a particular guest made by the restaurant"""

    __tablename__ = "guest_reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=False)
    score = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    

    restaurant = db.relationship("Restaurant", back_populates="guest_review")
    user = db.relationship("User", back_populates="guest_review")


    def __repr__ (self):
        return f"<Guest Review:{self.id}>"


class RestaurantReview(db.model):
    """a review of a particular restaurant made by the guest that dined there"""


    __tablename__ = "restaurant_reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text)
    

    restaurant = db.relationship("Restaurant", back_populates="restaurant_review")
    guest = db.relationship("Guest", back_populates="restaurant_review")


    def __repr__ (self):
        return f"<Restaurant Review:{self.id}>"
    

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///kickback"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")



if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
    





    