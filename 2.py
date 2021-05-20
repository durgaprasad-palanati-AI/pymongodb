import pymongo
from pymongo import MongoClient
from pymongo.message import update
'''
#create a client object to communicate with your currently running MongoDB instance
'''
client = MongoClient()
db = client.pydb1
users = db.user
#update one
users.update_one({'username':'durga3'},{"$set":{'role':'examiner'}})
#update many
users.update_many({'username':{'$regex':'2$'}},{"$set":{'role':'prinicipal'}})
#delete one
users.delete_one({'username':'durga3'})
#delete many
users.delete_many({'username':{'$regex':'1$'}})