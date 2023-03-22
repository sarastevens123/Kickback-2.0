import json
import model 
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

@app.route('/')
def homepage():
    """Display homepage"""
    pass










if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')