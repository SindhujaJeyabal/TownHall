#!/usr/bin/env python

import shelve
from subprocess import check_output
import flask
from flask import request
from os import environ
import sqlite3
from contextlib import closing
from db import *
from jinja2 import TemplateNotFound
from flask import abort
import time
import math
import string
import json

app = flask.Flask(__name__)
app.debug = True

@app.route('/')
def landing_page():
	return flask.render_template(
            'home.html')

@app.errorhandler(404)
def page_not_found(e):
	return flask.render_template('404.html', prefix = "URL not found", url=''), 404


if __name__ == "__main__":
    app.run();#port=int(environ['FLASK_PORT']))
