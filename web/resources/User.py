from flask_restful import Api, Resource
from flask import jsonify, request
from dappers.Dappers import UserDapper

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
    
class User(Resource):
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

