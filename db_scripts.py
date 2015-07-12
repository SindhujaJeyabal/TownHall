import sqlite3
from flask import g

DB_PATH = './townhall.db'

def create_table_status_table():
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	querytoExec="create table status (id not null, name not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def create_table_profile_table():
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	querytoExec="create table profiles (id not null, name not null, display_name not null, flagged not null, points not null, status not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def create_campaigns_table():
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	querytoExec="create table campaigns (id not null, owner not null, text not null, votes not null, max_votes not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def create_comments_table():
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	querytoExec="create table comments (id not null, owner not null, text not null, reply_to not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def create_tables()
	create_table_status_table();
	create_table_profile_table();
	create_campaigns_table();
	create_comments_table();

def populate_status_table()

	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	objtoadd= [('1','1'),('2','2'), ('3','3'),('4','4')]
	query='insert into status values (?,?)'
	c.executemany(query, objtoadd)
	conn.commit()
	conn.close()

def populate_profiles_table()

	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	objtoadd= [('1','jdoe', 'John', 'False', '10', '3'),
				('2','bshaw', 'Becca', 'True', '3', '4'), 
				('3','acloe', 'Alice', 'False', '50', '1')]
	query='insert into status values (?,?,?,?,?,?)'
	c.executemany(query, objtoadd)
	conn.commit()
	conn.close()

def populate_campaigns_table()

	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	objtoadd= [('1','1', 'Hey Campaign1....', '10', '30'),
				('2','3', 'Hey Campaign2....', '10', '30'),
				('3','2', 'Hey Campaign3....', '10', '30'),
				('4','3', 'Hey Campaign4....', '10', '30'),
				('5','1', 'Hey Campaign5....', '10', '30'),
				('6','3', 'Hey Campaign6....', '10', '30'),
			]
	query='insert into status values (?,?,?,?,?)'
	c.executemany(query, objtoadd)
	conn.commit()
	conn.close()

def populate_comments_table()
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	objtoadd= [('1','1', 'comment....', '1'),
				('2','2', 'comment....', '3'),
				('3','3', 'comment....', '3'),
				('4','3', 'comment....', '6'),
				('5','3', 'comment....', '2'),
				('6','1', 'comment....', '6'),
			]
	query='insert into status values (?,?,?,?)'
	c.executemany(query, objtoadd)
	conn.commit()
	conn.close()


def populate_tables()
	populate_status_table();
	populate_profiles_table();
	populate_campaigns_table();
	populate_comments_table();

def delete_status_table()
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	query='delete * from status'
	c.executemany(query)
	conn.commit()
	conn.close()

def delete_profiles_table()
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	query='delete * from profiles'
	c.executemany(query)
	conn.commit()
	conn.close()

def delete_campaigns_table()
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	query='delete * from campaigns'
	c.executemany(query)
	conn.commit()
	conn.close()

def delete_comments_table()
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	query='delete * from comments'
	c.executemany(query)
	conn.commit()
	conn.close()

def clear_tables()
	delete_status_table();
	delete_profiles_table();
	delete_campaigns_table();
	delete_comments_table();

def get_campaigns()
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	query='select * from campaigns'
	c.executemany(query)
	conn.commit()
	conn.close() 	

def get_agenda()

if __name__ == '__main__':

	create_tables();
	populate_tables();