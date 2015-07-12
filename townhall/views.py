	
from flask import render_template,request,session,redirect,jsonify,Response
from flask import url_for
from townhall import app
import urllib2
import math
import json
import dbhandler
import checkText

@app.route('/', methods=['GET', 'POST'])
def land():
	return render_template("landing.html")

@app.route('/campaigns', methods=['GET', 'POST'])
def campaigns():
	return render_template("index.html")

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
	return render_template("agenda.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	return render_template("admin.html")

@app.route('/flagged', methods=['GET'])
def flagged():
	return render_template("flagged.html")

@app.route('/new', methods=['GET'])
def create():
	print "creating a post...."
	return render_template("campaign.html", is_new = True, can_post = True)

@app.route('/error', methods=['GET'])
def check_abuse():
	can_post = True
	can_post = checkText.is_abusive("Stephanie Marc is bad")
	print can_post
	return render_template("campaign_error.html", is_new = False, can_post = False)