from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, json)
from model import connect_to_db, db


import crud
import os



#environment variables

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

#Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def homepage():

    return "This is the homepage"



@app.route('/login', methods=['POST'])
def login_user():
    """Login existing user."""

#Input fields for login
    email = request.json.get('email')
    password = request.json.get('password')

#Queries both guest, and restaurant tables to get user object
    guest_user = crud.get_guest_by_email(email)
    restaurant_user = crud.get_restaurant_by_email(email)

#Checks if the user if a guest
    if guest_user:
        if guest_user.password == password:
            session['user'] = guest_user.id
            return jsonify({
                            'id':guest_user.id,
                            'first name':guest_user.fname,
                        })
        else:
            return jsonify("Incorrect Password")
#Checks if a user is  a restaurant    
    if restaurant_user:
        if restaurant_user.password == password:
            session['user'] = restaurant_user.id
            return jsonify({
                            'id':restaurant_user.id,
                            'name':restaurant_user.name,
                        })
        else:
            return jsonify("Incorrect Password")
           
    else:
        return jsonify("Account does not exist.Try again, or create a new account.")
    


@app.route('/logout')
def logout_user():
    """Logs out a session user"""

    del session['user']

    return "User logged out from session"

@app.route('/create-guest')
def create_new_guest_user():

    email = request.json.get('email')
    password = request.json.get('password')
    fname = request.json.get('fname')
    lname = request.json.get('lname')


    if crud.get_guest_by_email(email):
        return jsonify({'alert':"Guest already exists."})
    else:
        guest = crud.create_guest_user(email,password,fname,lname)
        db.session.add(guest)
        db.session.commit(guest)

        return jsonify({'user_id' :f"{guest.id}"})
    

        












if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')