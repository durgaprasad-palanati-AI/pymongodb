import pymongo
from pymongo import MongoClient
from pymongo.message import update
import pprint
'''
#create a client object to communicate with your currently running MongoDB instance
'''
client = MongoClient()
db = client.pydb1
users = db.user
#update one -->change role of user
users.update_one({'username':'durga'},{"$set":{'role':'examiner'}})# does not return document
#update many --> change role of users whose name STARTS WITH "A"
users.update_many({'username':{'$regex':'^A'}},{"$set":{'role':'leader'}})
#delete one --> Delete particular user
users.delete_one({'username':'durga'})
#delete many --> Delete users whose name starts with "B"
users.delete_many({'username':{'$regex':'^B'}})