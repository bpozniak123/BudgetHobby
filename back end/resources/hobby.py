import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

hobby = Blueprint('hobby', 'hobby') #1st is blueprint name, 2nd is it's import_name

#GET route 
@hobby.route('/')
def hobby_index():
	result = models.Hobby.select()

	print('APP WORKS')
	print(result)