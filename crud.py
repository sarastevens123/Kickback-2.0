"""CRUD operations"""
from model import (db, Guest, GuestReview, Restaurant, RestaurantReview, connect_to_db)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload



def create_guest_user(fname, lname, password, email):
    """Create and return a new user."""

    guest = Guest(fname=fname, lname=lname, password=password, email=email)
    db.session.add(guest)
    db.session.commit()
    return guest


def return_guest_by_id(user_id):
    """"Returns a user by their ID."""

    return Guest.query.get(user_id)


def create_restaurant_user(name, email, password, location):
    """Create and return a new restaurant."""

    restaurant = Restaurant(name=name, email=email,password=password, location=location)
    db.session.add(restaurant)
    db.session.commit()
    return restaurant 

def return_all_guests():
    """"Return a list of all users."""

    return Guest.query.all()

def return_all_restaurants():
    """"Return a list of all restaurants."""

    return Restaurant.query.all()


def return_restaurant_by_id(restaurant_id):
    """"Returns a restaurant by its ID."""

    return Restaurant.query.get(restaurant_id)

def get_guest_by_email(email):
    """Return a user by their email, else returns None."""

    return Guest.query.filter(Guest.email == email).first()

def get_restaurant_by_email(email):
    """Return a restaurant by their email, else returns None."""

    return Restaurant.query.filter(Restaurant.email == email).first()

def get_guest_password(password):
    """Return User password."""

    return Guest.query.filter(Guest.password == password).first()

def get_restaurant_password(restaurant_password):
    """Return restaurant password."""

    return Restaurant.query.filter(Restaurant.restaurant_password == restaurant_password).first()

def create_restaurant_review(guest_id, restaurant_id, score, text):
    """Creates and returns a restaurant review."""
    
    review = RestaurantReview(guest_id=guest_id, restaurant_id=restaurant_id, score=score, text=text)
    db.session.add(review)
    db.session.commit()
    return review

def create_guest_review(restaurant_id, guest_id, score, text):
    """Creates and returns a guest review."""

    review = GuestReview(restaurant_id=restaurant_id, guest_id=guest_id, score=score, text=text)
    db.session.add(review)
    db.session.commit()

    return review

def get_average_restaurant_score(restaurant_id):
    """returns an average restaurant score"""
    total_scores = 0
    counter = RestaurantReview.query.filter_by(restaurant_id=restaurant_id).count()

    if counter > 0:
        reviews = RestaurantReview.query.filter_by(restaurant_id=restaurant_id).all()

        for review in reviews:
            total_scores = total_scores + int(review.score)

        avg = total_scores / counter

        return ("{:.1f}".format(avg))


def get_average_guest_score(user_id):
    """returns an average guest score"""
    total_scores = 0
    counter = GuestReview.query.filter_by(user_id=user_id).count()

    if counter > 0:
        reviews = GuestReview.query.filter_by(user_id=user_id).all()

        for review in reviews:
            total_scores = total_scores + int(review.score)
        
        avg = total_scores / counter

        return ("{:.1f}".format(avg))

def get_restaurant_id_by_name(name):

    restaurant = Restaurant.query.filter_by(name=name).first()
    

    return restaurant.id

    
 

    
    
    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)