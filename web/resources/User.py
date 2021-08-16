from flask_restful import Api, Resource
from flask import jsonify, request

# tenderResults,
# toughResults,
# intuitionResult,
# sensingResult,
# introvertResult,
# extrovertResult,

def check_posted_data():
    props = ('email', 'tenderResults', 'toughResults', 'intuitionResult', 'sensingResult', 'introvertResult', 'extrovertResult')
    dict = request.get_json()
    if props not in dict:
        return 'ERROR', 404
    return jsonify(dict), 200
    
class User(Resource):
    def post(self, userDapper):
        dict = request.get_json()
        status_code = check_posted_data(dict)
        if status_code != 200:
            return {
                'result': "Invalid request body",
                "status_code": status_code
            }, status_code

        user = userDapper.findOne({'email' : dict.email});
        if(user):
            return {
                'result': "User already exist",
                "status_code": status_code
            }, status_code
        res = userDapper.insert(user) 
        # Usernumber.update({}, {
        #     "$set": {
        #         "num_of_users": prev_num
        #         }
        #     })
        return jsonify(res), 200

