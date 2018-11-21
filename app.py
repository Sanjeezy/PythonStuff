from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

uri = 'mongodb://testUser1:testUser1@ds031183.mlab.com:31183/api_test'


@app.route('/users', methods=['GET'])
def get_all_users():
	client = pymongo.MongoClient(uri)
	db = client.get_default_database()
	output = []

	userRecords = db['userRecords']
	
	for record in userRecords.find():
		output.append({
			'First_Name' : record['first_name'],
			'middle_name' : record['middle_name'],
			'Last_Name' : record['last_name'],
			'ssn' : record['ssn'],
			'email' : record['email'],
			'Phone' : record['phone'],
			'Date of Birth' : record['dob'] 
		})

	client.close()
	return jsonify({'result' : output})



@app.route('/users/<name>', methods=['GET'])
def get_single_user(name):
	client = pymongo.MongoClient(uri)
	db = client.get_default_database()
	userRecords = db['userRecords']

	record = userRecords.find_one({'first_name' : name})

	if record:
		output = ({
				'first_Name' : record['first_name'],
				'middle_name' : record['middle_name'],
				'Last_Name' : record['last_name'],
				'ssn' : record['ssn'],
				'email' : record['email'],
				'Phone' : record['phone'],
				'Date of Birth' : record['dob'] 
		})
	else:
		output = "No record with that name found"
	client.close()
	return jsonify({'result' : output})


@app.route('/users', methods=['POST'])
def add_user():
	client = pymongo.MongoClient(uri)
	db = client.get_default_database()
	userRecords = db['userRecords']

	#Parse user details from request
	first_name = request.json['first_name']
	middle_name = request.json['middle_name']
	last_name = request.json['last_name']
	ssn = request.json['ssn']
	email = request.json['email']
	phone = request.json['phone']
	dob = request.json['dob']

	#insert new user into DB
	userRecordId = userRecords.insert({
		'first_name' : first_name,
		'middle_name' : middle_name,
		'last_name' : last_name,
		'ssn' : ssn,
		'email' : email,
		'phone' : phone,
		'dob' : dob 
	})

	print(first_name)
	print(userRecordId)

	new_record = userRecords.find_one({'_id' : userRecordId})

	if new_record:
		output = ({
				'first_name' : new_record['first_name'],
				'middle_name' : new_record['middle_name'],
				'last_Name' : new_record['last_name'],
				'ssn' : new_record['ssn'],
				'email' : new_record['email'],
				'phone' : new_record['phone'],
				'dob' : new_record['dob'] 
		})
	else:
		output = "Record was not able to be added to db"

	client.close()
	return jsonify({'result' : output})


if __name__ == '__main__':
	app.run(debug=True)
	





# def main():
# 	client = pymongo.MongoClient(uri)
# 	db = client.get_default_database()
	
# 	userRecords = db['userRecords']
# 	userRecords.insert({
#         "first_name": "Allen",
# 	    "middle_name": "Paul",
# 	    "last_name": "Gates",
# 	    "ssn": "113-11-1411",
# 	    "email": "allen@paul.org",
# 	    "phone": "(408) 111-1131",
# 	    "dob": "10/02/1997"
#     })
	
# 	userRecords.find()

# 	print("added record")

# 	client.close()