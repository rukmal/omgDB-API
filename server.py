from flask import Flask, request
import redis

from flask.ext.restful import Resource, Api

app = Flask(__name__, static_url_path='')
api = Api(app)

# Handling landing page routing
@app.route('/')
def landingpage():
	return app.send_static_file('index.html')

# Handling the generation of new IDs
@app.route('/gettoken', methods=['POST'])
def authtoken():


if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=3000)