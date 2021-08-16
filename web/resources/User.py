from flask.wrappers import Response
from flask_restful import Api, Resource
from flask import jsonify, request
from dappers.Dappers import UserDapper
import json, sys
from bson import json_util

# tenderResults,
# toughResults,
# intuitionResult,
# sensingResult,
# introvertResult,
# extrovertResult,

def check_posted_data(dict):
    found = list()
    props = ('email', 'tenderResults', 'toughResults', 'intuitionResult', 'sensingResult', 'introvertResult', 'extrovertResult')
    dict = request.get_json()
    if 'email' not in dict:
        return 422
    return 200

def build_response(data, status_code):
    response = {
            'data': data,
            "status_code": status_code
        }, status_code
    return jsonify(response)

class User(Resource):

    '''
    Let's find all users. Find() will return a pymongo.cursor.Cursor 
    We'll get the actual objects by iterating over the cursor to get its results:
    '''
    def get(self):
        # print([doc for doc in UserDapper.user_collection().find()])
        users = [doc for doc in UserDapper.user_collection().find()]
        # users = UserDapper.user_collection().find()
        resp = Response(json.dumps({'data': users}, default=json_util.default),
                mimetype='application/json')
        return resp

    def post(self):
        dict = request.get_json()
        status_code = check_posted_data(dict)
        if status_code != 200:
            return {
                'result': "Invalid request body",
                "status_code": status_code
            }, status_code
        print(dict);
        user = UserDapper.user_collection().find_one({'email' : dict['email']});
        if(user):
            return {
                'result': "User already exist",
                "status_code": status_code
            }, status_code
        res = UserDapper.user_collection().insert_one(dict) 
        response = {
            'id': str(res.inserted_id),
            "status_code": status_code
        }, status_code
        return response

