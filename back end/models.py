import os
from playhouse.db_url import connect
from peewee import *

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///hobbiesDB.sqlite')

class Hobby(Model):
	hobby = CharField(unique = True)
	type_of_hobby = CharField (unique = False)
	tools = CharField (unique = True)
	cost_of_tools = CharField (unique = True)
	accessories = CharField (unique = True)

	class Meta:
		database = DATABASE

# class Budget(Model):



def initialize():
	DATABASE.connect()

	DATABASE.create_tables([Hobby], safe=True)
	print("Connected to database and created tables if they did not exist")

	DATABASE.close()