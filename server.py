from flask import Flask, render_template
from jinja2 import Template
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Handling base page routing
@app.route('/')
def landingpage():
	return render_template('docs/developers.html')

if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=3000)