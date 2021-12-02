from flask import Flask, jsonify

from resources.hobby import hobby
from resources.budget import budget

import os 

import models

from flask_cors import CORS

# from flask_login import LoginManager

from dotenv import load_dotenv

load_dotenv() #takes the environment variables from .env

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_APP_SECRET")
print(os.environ.get("FLASK_APP_SECRET"))

# CORS -- Cross Origin Resource Sharing
# a web domain (site/port/etc) is an "origin"
# this app is localhost:8000, that's an origin
# our react app is localhost:3000, that's a different origin
# Browsers implement CORS to prevent an JS app from sending requests
  # to origins other than the one the browser originally went to to get that JS
  # configuring CORS lets server say "here's who i'm expecting to hear from"

# first arg -- we are adding cors to blueprints, which blueprint to use
  # (you can CORS the whole app too)
# second arg -- which origins are allowed
# third arg -- lets us accept requests with cookies attached (so that we can
  # use sessions for auth)
CORS(hobby, origins= ['http://localhost:3000'], support_credentials=True)
# CORS(users, origins=['http://localhost:3000'], support_credentials=True)



if __name__ == '__main__':
	models.initialize() 
	app.run(debug=DEBUG, port=PORT)
