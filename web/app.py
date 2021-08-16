from resources.User import User
from resources.Add import Add
from flask import Flask, app, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# Communicate with the Mongo docker db service
client = MongoClient('mongodb://db:27017')
# Create new Database
db = client.aNewDB
# Create new collection
UserDapper = db['Users']

# @app.route('/users', methods=['POST'])
@app.route('/')
def default():
    return 'Friendy service for managing  Hi!'


#Endpoint resources
api.add_resource(User, '/user')

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=3000, debug=True)
    app.run(host="0.0.0.0", port= 5001, debug=True)