	
from flask import render_template,request,session,redirect,jsonify,Response
from flask import url_for
from townhall import app
import urllib2
import math
import json
import dbhandler

@app.route('/', methods=['GET', 'POST'])
def land():
	campaigns, agenda = dbhandler.get_campaigns_agenda();

	return render_template("landing.html", campaigns = campaigns, agenda = agenda)