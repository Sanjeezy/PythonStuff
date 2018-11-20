from flask import jsonify
from flask import Blueprint
from flask_restful import Resource, Api, reqparse

import models

class CourseList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'title',
			required=True,
			help='No Title Provided',
			location=['form', 'json']	#specifies content type
		)
		self.reqparse.add_argument(
			'url',
			required=True,
			help='No course url provided',
			location=['form','json']
		)
		super(CourseList, self).__init__()


	def get(self):
		return jsonify({'courses' : [{'title' : 'Python Basics'}]})

class Course(Resource):
	def get(self, id):
		return jsonify({'title' : 'Python Basics'})

	def put(self, id):
		return jsonify({'title' : 'Python Basics'})

	def delete(self, id):
		return jsonify({'title' : 'Python Basics'})

courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)

api.add_resource(
	CourseList,
	'/api/v1/courses',
	endpoint='courses'
	)

api.add_resource(
	Course,
	'/api/v1/<int:id>',
	endpoint='course'
	)