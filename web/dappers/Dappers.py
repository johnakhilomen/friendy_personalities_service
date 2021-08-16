from pymongo import MongoClient

# Communicate with the Mongo docker db service
client = MongoClient('mongodb://db:27017')
# Create new Database
db = client.aNewDB

# Create new collection
class UserDapper:
    def user_collection():
        return db['Users']