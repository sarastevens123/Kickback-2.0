import json
import model 
from jijnja import StrictUndefined
from flask import Flask, render_template,jsonify,request,session,flash,send_from_directory

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

#Jinja templating debugging assist
app.jinja_env.undefined = StrictUndefined