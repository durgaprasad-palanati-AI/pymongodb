import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.pydb1
users = db.user
updoc=users.find_one_and_update({'username':'A.Ram'},{"$set":{'role':'teacher'}},{'return_document':'true'})