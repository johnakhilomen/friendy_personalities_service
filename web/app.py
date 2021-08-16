from resources.User import User
from flask import Flask, app, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# @app.route('/users', methods=['POST'])
@app.route('/')
def default():
    return 'Friendy service for managing  Hi!'

#Endpoint resources
api.add_resource(User, '/user')

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=3000, debug=True)
    app.run(host="0.0.0.0", debug=True)