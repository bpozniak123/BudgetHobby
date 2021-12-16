import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

hobby = Blueprint('hobby', 'hobby') #1st is blueprint name, 2nd is it's import_name

#GET route 
@hobby.route('/')
def hobby_index():
	result = models.Hobby.select()
	hobby_list = [model_to_dict(hobby) for hobby in result]

	print(hobby_list)
	return jsonify(hobby_list)

#----------------------------------
#CREATE route
@hobby.route('/', methods=['POST'])
def new_hobby():
	payload = request.get_json()
	print(payload)
	result = models.Hobby.create(
		hobby = payload['hobby'], 
		type_of_hobby = payload['type_of_hobby'], 
		tools = payload['tools'], 
		cost_of_tools = payload['cost_of_tools'], 
		gear = payload['gear'], 
		cost_of_gear = payload['cost_of_gear'],
		accessories = payload['accessories'],
		cost_of_accessories = payload['cost_of_accessories']
	)
	result_dict = model_to_dict(result)
	print(result)
	return jsonify(
		# result
		data = result_dict,
		status = 201,
		message = "Created a hobby!"
	), 201

#----------------------------------
#SHOW route
@hobby.route('<id>', methods=['GET'])
def show_hobby(id):
	hobby = models.Hobby.get_by_id(id)
	print(hobby)
	
	return jsonify(
		data = model_to_dict(hobby),
		message = 'Show Route Success!',
		status = 200
	), 200

#----------------------------------
#UPDATE route 
@hobby.route('/<id>', methods=['PUT'])
def update_hobby(id):
	payload = request.get_json()
	models.Hobby.update(**payload).where(models.Hobby.id==id).execute()
	
	return jsonify(
		data = model_to_dict(models.Hobby.get_by_id(id)),
		message = 'Hobby Updated!',
		status = 200,
	), 200

#----------------------------------
#DELETE route
@hobby.route('/<id>', methods=['DELETE'])
def delete_hobby(id):
	delete_query = models.Hobby.delete().where(models.Hobby.id == id)
	num_of_rows_deleted = delete_query.execute()
	print(num_of_rows_deleted)

	return jsonify(
		data = {},
		message = f"Deleted {num_of_rows_deleted} hobby with this id {id}",
		status = 200
	), 200
