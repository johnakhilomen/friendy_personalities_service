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
Usernumber = db['UserNumbers']

# test insertion 
Usernumber.insert({
    'num_of_users' : 0
})


class Visit(Resource):
    def get(self):
        prev_num = Usernumber.find({})[0]['num_of_users']
        prev_num+=1
        Usernumber.update({}, {
            "$set": {
                "num_of_users": prev_num
                }
            })
        return str("Hello user " + str(prev_num))


@app.route('/')
def hello():
    return 'Just Hi!'

@app.route('/users', methods=['POST'])
def add_user():
    dict = request.get_json()
    if 'firstName' not in dict:
        return 'ERROR', 404
    return jsonify(dict), 200
    
@app.route('/json')
def jsonData():
    json = [
        {
        "userId":"rirani",
        "jobTitleName":"Developer",
        "firstName":"Romin",
        "lastName":"Irani",
        "preferredFullName":"Romin Irani",
        "employeeCode":"E1",
        "region":"CA",
        "phoneNumber":"408-1234567",
        "emailAddress":"romin.k.irani@gmail.com"
        },
        {
        "userId":"nirani",
        "jobTitleName":"Developer",
        "firstName":"Neil",
        "lastName":"Irani",
        "preferredFullName":"Neil Irani",
        "employeeCode":"E2",
        "region":"CA",
        "phoneNumber":"408-1111111",
        "emailAddress":"neilrirani@gmail.com"
        },
        {
        "userId":"thanks",
        "jobTitleName":"Program Directory",
        "firstName":"Tom",
        "lastName":"Hanks",
        "preferredFullName":"Tom Hanks",
        "employeeCode":"E3",
        "region":"CA",
        "phoneNumber":"408-2222222",
        "emailAddress":"tomhanks@gmail.com"
        }
        ]
    return jsonify(json), 200


# Math stuff
api.add_resource(Add, '/add')
api.add_resource(Visit, '/visit')

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=3000, debug=True)
    app.run(host="0.0.0.0", debug=True)