
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, json)
from model import connect_to_db, db
import crud
import os

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'












if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')