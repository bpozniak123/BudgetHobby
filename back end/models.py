import os
from playhouse.db_url import connect
from peewee import *

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///hobbiesDB.sqlite')

class Hobby(Model):
	hobby = CharField(unique = True)
	type_of_hobby = CharField (unique = False)
	tools = CharField (unique = True)
	cost_of_tools = IntegerField (unique = True)
	gear = CharField (unique = True)
	cost_of_gear = IntegerField (unique = True)
	accessories = CharField (unique = True)
	cost_of_accessories = IntegerField (unique = True)

	class Meta:
		database = DATABASE

# class Budget(Model):
class Budget(Model):


	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()

	DATABASE.create_tables([Hobby], safe=True)
	print("Connected to database and created tables if they did not exist")

	DATABASE.close()