import pymongo
from pymongo import MongoClient
import pprint
'''
#create a client object to communicate with your currently running MongoDB instance
'''
client = MongoClient()
db = client.pydb1
users = db.user

print("--------------1.findone--users whose initial is 'A'---------")
#find users whose initial is "A"
user_A = users.find_one({"username": {"$regex":"^A"}})
pprint.pprint(user_A)
#>>>
'''
{'_id': ObjectId('60a6676724966527325584ad'),
 'role': 'leader',
 'username': 'A.Ram'}
'''
print("--------------2.findone--users whose name ends with  'l'---------")
#find users whose name ends with  "l"
user_b = users.find_one({"username": {"$regex":"l$"}})
pprint.pprint(user_b)
#>>>
'''
{'_id': ObjectId('60a6676724966527325584ae'),
 'role': 'leader',
 'username': 'A.Shyaml'}
'''
print("--------------find-----------")
#find users whose name ends with  "m"
user_c = users.find({"username": {"$regex":"^A"}})# return cursor <pymongo.cursor.Cursor object at 0x00000092DBD6EE08>
for doc in user_c:  #iterrate through cursor to get docs
    pprint.pprint(doc)
#>>>
'''
{'_id': ObjectId('60a6676724966527325584ad'),
 'role': 'leader',
 'username': 'A.Ram'}
{'_id': ObjectId('60a6676724966527325584ae'),
 'role': 'leader',
 'username': 'A.Shyaml'}
'''