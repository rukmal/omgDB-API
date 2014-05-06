from flask import Flask, request

from flask.ext.restful import Resource, Api

app = Flask(__name__, static_url_path='')
api = Api(app)

# Handling base page routing
@app.route('/')
def landingpage():
	return app.send_static_file('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=3000)