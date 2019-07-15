import os
import hashlib
import logging
import json
from datetime import datetime
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, json, jsonify, abort, make_response

from magneto.ADN import ADN


app = Flask(__name__,template_folder="/app-run/api/templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)


class Stats(db.Model):
    __tablename__ = 'stats'

    id = db.Column('stat_id',db.Integer,primary_key=True)
    isMutant = db.Column('is_mutant',db.Boolean,nullable=False)
    register = db.Column('register', db.DateTime,nullable=False)
    dna = db.Column('dna', db.String,nullable=False)
    dnaHash = db.Column('dna_hash', db.String,nullable=False)

    def saveStat(self):
        hash_object = hashlib.md5(str(self.dna).encode())
        self.register =  datetime.now()
        self.dnaHash = hash_object.hexdigest()
        db.session.add(self)
        db.session.commit()
    
    def getByDNA(self):
        hash_object = hashlib.md5(str(self.dna).encode())
        item = Stats.query \
                  .filter_by(dnaHash=hash_object.hexdigest()) \
                  .first()
        return item

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
    #print( content )
    stats = Stats(dna=request.data)

    stat = stats.getByDNA()

    if stat is None:
        if 'dna' not in content:
            stats.isMutant = False
        else:
            stats.isMutant = ADN.isMutant(content['dna'])
        stats.saveStat()
    else:
        #print('already exists')
        stats = stat


    if stats.isMutant:
        response = app.response_class(response=json.dumps({'mutante':True}),
            status=200,
            mimetype='application/json')
    else:
        response = app.response_class(response=json.dumps({'mutante':False}),
            status=403,
            mimetype='application/json')

    return response



