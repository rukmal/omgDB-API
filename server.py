from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class LandingPage(restful.Resource):
	def get(self):
		return {'hello': 'world'}

api.add_resource(LandingPage, '/')

if __name__ == '__main__':
	# Code for running on Heroku
	# app.run(debug=False, port=3000)
	# Code for running locally with debugging
	app.run(debug=True, host='0.0.0.0', port=3000)