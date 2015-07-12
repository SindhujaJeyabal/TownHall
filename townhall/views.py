	
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

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	return render_template("admin.html")

@app.route('/new', methods=['GET'])
def create():
	print "creating a post...."
	return render_template("create.html", is_new = True, can_post = True)

@app.route('/new', methods=['POST'])
def check_abuse():
	n = request.form.get('campaign_text')
	# app.send_static_file
	print n
	can_post = True
	can_post = checkText.is_abusive(n)
	print can_post
	return render_template("create.html", is_new = False, can_post = can_post)