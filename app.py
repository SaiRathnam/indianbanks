import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import helpers

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models

# To check if the app is up
@app.route("/")
def hello():
    data = {"message": "Hello World"}
    return jsonify(data), 200

# API 1: Given an IFSC Code, returns the branch details
@app.route("/v1/banks/branches/<ifsc_code>", methods=['GET'])
def get_branch_details(ifsc_code):
	if len(ifsc_code) != 11:
		data = {"message": "Invalid IFSC code. Enter correct IFSC code."}
		return jsonify(data), 200
	
	if helpers.invalid_character_in_ifsc(ifsc_code):
		data = {"message": "Invalid IFSC code. Enter correct IFSC code."}
		return jsonify(data), 200

	else:
		try:
			branch = models.Branch.query.filter_by(ifsc=ifsc_code).first()
			if branch is not None:
				branch_details = branch.serialize()
				data = {"branch": branch_details}
				return jsonify(data), 200
			else:
				data = {"message": "There was no bank found with that IFSC code"}
				return jsonify(data), 200
		except Exception as e:
			# For debugging later from the logs
			print(str(e))
			data = {"message": "Internal server error"}
			return jsonify(data), 500

# API 2: Given a bank name and city, returns all branches
@app.route("/v1/banks/all_branches", methods=['GET'])
def get_all_branches():
	try:
		bank_name = request.args.get('bank_name')
		city = request.args.get('city')

		if len(bank_name) < 1:
			data = {"message": "Invalid bank name."}
			return jsonify(data), 200
		else:
			bank_name = bank_name.upper()
		if len(city) < 1:
			data = {"message": "Invalid city name."}
			return jsonify(data), 200
		else:
			city = city.upper()

		bank = models.Bank.query.filter_by(name=bank_name).first()
		if bank is not None:
			bank_id = bank.get_id()
			branches = models.Branch.query.filter_by(bank_id=bank_id, city=city).all()
			if len(branches) >= 1:
				all_branches = []
				for branch in branches:
					all_branches.append(branch.serialize())
				data = {"branches": all_branches}
				return jsonify(data), 200
			else:
				data = {"message": "There were no branches found for this bank."}
				return jsonify(data), 200
		else:
			data = {"message": "There was no bank found."}
			return jsonify(data), 200
	
	except Exception as e:
		# For debugging later from the logs
		print(str(e))
		data = {"message": "Internal server error"}
		return jsonify(data), 500


if __name__ == '__main__':
	app.run()
