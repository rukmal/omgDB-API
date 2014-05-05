from flask import Flask
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class LandingPage(Resource):
	def get(self):
		return {'hello':'world'}

api.add_resource(LandingPage, '/')

if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=3000)