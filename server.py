from flask import Flask, request
from flask.ext.restful import Resource, Api
import redis

# Connecting to the redis store (for api keys)
red = redis.StrictRedis(host='pub-redis-19603.us-east-1-4.3.ec2.garantiadata.com', port=19603, db=0)

app = Flask(__name__, static_url_path='')
api = Api(app)

# Handling landing page routing
@app.route('/')
def landingpage():
	return app.send_static_file('index.html')

# Handling the generation of new IDs
# @app.route('/gettoken', methods=['POST'])
# def authtoken():

if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=3000)