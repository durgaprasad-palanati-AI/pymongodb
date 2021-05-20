import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.pydb1
users = db.user #db.cllection-name
'''
use .find(). Without arguments, 
.find() returns a Cursor object that yields the documents in the collection on demand
'''
for doc in users.find():
    pprint.pprint(doc)
#>>>
'''
{'_id': ObjectId('60a6676724966527325584ac'),
 'role': 'Teacher',
 'username': 'durga'}
{'_id': ObjectId('60a6676724966527325584ad'),
 'role': 'student',
 'username': 'A.Ram'}
{'_id': ObjectId('60a6676724966527325584ae'),
 'role': 'student',
 'username': 'A.Shyam'}
{'_id': ObjectId('60a6676724966527325584af'),
 'role': 'teacher',
 'username': 'B.Gani'}
{'_id': ObjectId('60a6676724966527325584b0'),
 'role': 'teacher',
 'username': 'B.Kiran'}
{'_id': ObjectId('60a6676724966527325584ac'),
 'role': 'Teacher',
 'username': 'durga'}
'''
user_1 = users.find_one({"username": "durga"})
pprint.pprint(user_1)
#>>>
'''
{'_id': ObjectId('60a6676724966527325584ac'),
 'role': 'Teacher',
 'username': 'durga'}
 '''