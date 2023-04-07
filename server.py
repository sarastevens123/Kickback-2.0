from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, json)
from model import connect_to_db, db

import crud


app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

@app.route('/')
def homepage():

    return "This is the homepage"

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