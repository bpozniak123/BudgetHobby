import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

budget = Blueprint('budget', 'budget') #1st is blueprint name, 2nd is it's import_name

#GET route 
@budget.route('/')
def budget_index():
	return 'budget'

#----------------------------------
#CREATE route
@budget.route('/', methods=['POST'])
def new_budget():
	payload = request.get_json()
	result = models.Budget.create(payload)
	return jsonify(
		result
	)

#----------------------------------
#SHOW route
@budget.route('<id>', methods=['GET'])
def show_budget(id):
	budget = models.Budget.get_by_id(id)
	print(budget)
	
	return jsonify(

	)

#----------------------------------
#UPDATE route 
@budget.route('/<id>', methods=['PUT'])
def update_budget(id):
	payload = request.get_json()
	models.Budget.update(**payload).where(models.Budget.id==id).execute()
	
	return jsonify(

	)

#----------------------------------
#DELETE route
@budget.route('/<id>', methods=['DELETE'])
def delete_budget(id):


	return jsonify(

	)