import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

hobby = Blueprint('hobby', 'hobby') #1st is blueprint name, 2nd is it's import_name

#GET route 
@hobby.route('/')
def hobby_index():
	result = models.Hobby.select()

	return jsonify(result)

#----------------------------------
#CREATE route
@hobby.route('/', methods=['POST'])
def new_hobby():
	payload = request.get_json()
	rtn = models.Hobby.create(payload)
	return jsonify(
		rtn
	)

#----------------------------------
#SHOW route
@hobby.route('<id>', methods=['GET'])
def show_hobby(id):
	hobby = models.Hobby.get_by_id(id)
	print(hobby)
	
	return jsonify(

	)

#----------------------------------
#UPDATE route 
@hobby.route('/<id>', methods=['PUT'])
def update_hobby(id):


	return jsonify(

	)

#----------------------------------
#DELETE route
@hobby.route('/<id>', methods=['DELETE'])
def delete_hobby(id):


	return jsonify(

	)
