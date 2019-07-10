# home blueprint accessed with route /
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app, make_response
import json
from os import environ as env
from flask_cors import cross_origin
# imports authentication utilitites to protect routes
from auth_utils import *

bp = Blueprint('main', __name__, url_prefix="/")
 

@bp.route('/')
def homepage():
    bprints = current_app.blueprints.keys()
    routes = sorted(set([str(p) for p in current_app.url_map.iter_rules()]))
    return render_template('index.html', routes=routes, bprints=bprints)

@bp.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# Controllers API
@bp.route("/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def public():
    """No access token required to access this route
    """
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)


@bp.route("/private")
@cross_origin(headers=["Content-Type", "Authorization"])
# hard coded web address here, need to check it out! CORS STUFF
# Acess-Control-Allow-Origin *?
@cross_origin(headers=["Access-Control-Allow-Origin", "http://0.0.0.0:5000"])
@requires_auth
def private():
    """A valid access token is required to access this route
    """
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)








#@bp.route('/post1', methods=['POST'])
#def post():
    # basic post request example
 #   try:
  #      url = request.form['url']
   # except:
    #    return jsonify({'Error':'Invalid POST request, send body as {"url": <url_of_pdf>}'})
    
    #return jsonify({'url':url})
