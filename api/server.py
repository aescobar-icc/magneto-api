import os
import logging
import json
from datetime import timedelta
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, json, jsonify, abort, make_response

from magneto.ADN import ADN


app = Flask(__name__,template_folder="/app-run/api/templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True 

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    domain:port/

    :return:        the rendered template 'index.html'
    """
    return render_template('index.html')

@app.route("/mutant/", methods=["POST"], strict_slashes=False )
def isMutant():
    content = request.json
    print( content )
    if 'dna' in content and ADN.isMutant(content['dna']) :
        response = app.response_class(response=json.dumps({'mutante':True}),
            status=200,
            mimetype='application/json')
    else:
        response = app.response_class(response=json.dumps({'mutante':False}),
            status=403,
            mimetype='application/json')

    return response



