from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')	#<name> signifies passing in a query to the route, without using ? in URL
def index(name="Treehouse"):
	return render_template("index.html",name=name)


	# name = request.args.get('name', name)
	#return "Hello from {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
	return render_template("add.html", num1=num1, num2=num2)






	# return """
	# <!doctype html>
	# <html>
	# <Head><title>Adding</title></head>
	# <body>
	# <h1>{} + {} = {}</h1>
	# </body>
	# </html>
	# """.format(num1, num2, num1+num2)




app.run(debug=True, port=8000, host='127.0.0.1')


