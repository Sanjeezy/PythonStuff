#Flask REST API
from flask import Flask
import models
from resources.courses import courses_api
from resources.reviews import reviews_api

DEBUG = True
HOST = '127.0.0.1'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')

@app.route('/')
def hello_world():
	return 'Hello world'


if __name__ == '__main__':
	models.initalize()
	app.run(debug=DEBUG, host=HOST, port=PORT)

