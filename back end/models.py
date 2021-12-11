import os
from playhouse.db_url import connect
from peewee import *

# DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///hobbiesDB.sqlite')
DATABASE = SqliteDatabase('hobbiesDB.sqlite')

class Hobby(Model):
	hobby = CharField(unique = True)
	type_of_hobby = CharField (unique = False)
	tools = CharField()
	cost_of_tools = IntegerField()
	gear = CharField (unique = False)
	cost_of_gear = IntegerField()
	accessories = CharField (unique = False)
	cost_of_accessories = IntegerField()
	

	class Meta:
		database = DATABASE
"""
	def select():
		cur = DATABASE.cursor()
		cur.execute('''SELECT * FROM hobby''')
		rslt = cur.fetchone()
		return rslt
		#return DATABASE.select('SELECT * FROM hobby')

	def create(payload):
		hobby = payload['hobby']
		hobbyType = payload['type_of_hobby']
		cost_of_tools = payload['cost_of_tools']
		tools = payload['tools']
		accessories = payload['accessories']
		query = f"INSERT INTO hobby (hobby, type_of_hobby, cost_of_tools, tools, accessories) VALUES ('{hobby}','{hobbyType}', '{cost_of_tools}', '{tools}', '{accessories}');"
		cur = DATABASE.cursor()
		cur.execute(query)
		return True
"""
"""
		if cur.index_id
			return true
		else
			return false
"""


class Budget(Model):
	name = CharField(unique = True)
	housing = IntegerField ()
	transportation = IntegerField ()
	grocery = IntegerField()
	utilities = IntegerField ()
	phone = IntegerField ()
	entertainment = IntegerField ()
	hobby_name = CharField(unique = True)
	hobby_tools_cost = IntegerField ()
	hobby_gear_cost = IntegerField ()
	hobby_accessories_cost = IntegerField ()
	maintenance_cost = IntegerField ()

	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()

	DATABASE.create_tables([Hobby, Budget], safe=True)
	print("Connected to database and created tables if they did not exist")

	DATABASE.close()