import 
import json
import model 
from flask import Flask, render_template,jsonify,request,session,flash,send_from_directory

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

