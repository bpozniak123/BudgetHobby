import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

budget = Blueprint('budget', 'budget') #1st is blueprint name, 2nd is it's import_name

#GET route 
@budget.route('/')
def budget_index():
	result = models.Budget.select()
	budget_list = [model_to_dict(budget) for budget in result]
	print(budget_list)
	return jsonify(budget_list)

#----------------------------------
#CREATE route
@budget.route('/', methods=['POST'])
def new_budget():
	payload = request.get_json()
	result = models.Budget.create(
		name = payload['name'],
		housing = payload['housing'],
		transportation = payload['transportation'],
		grocery = payload['grocery'],
		utilities = payload['utilities'],
		phone = payload['phone'],
		entertainment = payload['entertainment'],
		hobby_name = payload['hobby_name'],
		hobby_tools_cost = payload['hobby_tools_cost'],
		hobby_gear_cost = payload['hobby_gear_cost'],
		hobby_accessories_cost = payload['hobby_accessories_cost'],
		maintenance_cost = payload['maintenance_cost'],
	)
	print(result)
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
		data = model_to_dict(budget),
		message = 'Show Route Success!',
		status = 200
	), 200

#----------------------------------
#UPDATE route 
@budget.route('/<id>', methods=['PUT'])
def update_budget(id):
	payload = request.get_json()
	models.Budget.update(**payload).where(models.Budget.id==id).execute()
	
	return jsonify(
		data = model_to_dict(models.Budget.get_by_id(id)),
		message = 'Budget Updated!',
		status = 200,
	), 200

#----------------------------------
#DELETE route
@budget.route('/<id>', methods=['DELETE'])
def delete_budget(id):
	delete_query = models.Budget.delete().where(models.Budget.id == id)
	num_of_rows_deleted = delete_query.execute()
	print(num_of_rows_deleted)

	return jsonify(
		data = {},
		message = f"Deleted {num_of_rows_deleted} budget with this id {id}",
		status = 200
	), 200