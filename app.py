from flask import Flask, jsonify, after_this_request

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
app.register_blueprint(hobby, url_prefix='/api/v1/hobby/')
app.register_blueprint(budget, url_prefix='/api/v1/budget/')

app.secret_key = os.environ.get("FLASK_APP_SECRET")
app.config['SESSION_COOKIE_SAMESITE'] = "None"
app.config['SESSION_COOKIE_SECURE'] = True
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
CORS(app, origins= ['http://localhost:3000'], support_credentials=True)
# CORS(users, origins=['http://localhost:3000'], support_credentials=True)

@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)
                      
# ADD THESE THREE LINES -- because we need to initialize the
# tables in production too!
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
