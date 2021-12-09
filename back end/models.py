import os
from playhouse.db_url import connect
from peewee import *

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///hobbiesDB.sqlite')
#db = SqliteDatabase('hobbiesDB.sqlite')

class Hobby(Model):
	"""
	hobby = CharField(unique = True)
	type_of_hobby = CharField (unique = False)
	tools = CharField (unique = True)
	cost_of_tools = IntegerField (unique = True)
	gear = CharField (unique = True)
	cost_of_gear = IntegerField (unique = True)
	accessories = CharField (unique = True)
	cost_of_accessories = IntegerField (unique = True)
	"""

	class Meta:
		database = DATABASE

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
		if cur.index_id
			return true
		else
			return false
"""



# class Budget(Model):
# class Budget(Model):
# 	housing = 
# 	transportation =
# 	food = 
# 	utilities =
# 	hobby_main_item =
# 	hobby_gear =
# 	hobby_accessories = 

# 	class Meta:
# 		database = DATABASE


def initialize():
	DATABASE.connect()

	DATABASE.create_tables([Hobby], safe=True)
	print("Connected to database and created tables if they did not exist")

	DATABASE.close()