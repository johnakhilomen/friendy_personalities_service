from flask_restful import Api, Resource
from flask import request, jsonify

def check_posted_data(dict):
    if 'x' not in dict or 'y' not in dict:
        return 404
    else:
        return 200

class Add(Resource):
    def post(self):
        dict = request.get_json()
        status_code = check_posted_data(dict)
        if status_code != 200:
            return {
                'result': "x or y is missing",
                "status_code": status_code
            }, status_code
        x = int(dict['x'])
        y = int(dict['y'])
        sum = x + y
        response = {
            'result': sum,
            "status_code": status_code
        }, status_code
        return jsonify(response)