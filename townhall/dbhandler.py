import sqlite3
from flask import g
import db_scripts

def reset_data():
	db_scripts.clear_tables();
	db_scripts.populate_tables();

def get_campaigns_agenda():
	db_scripts.get_campaigns();
	db_scripts.get_agenda();

if __name__ == '__main__':

	pass
	# addUserGroupTable()
	

