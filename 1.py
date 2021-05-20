import pymongo
from pymongo import MongoClient
import pprint
'''
#create a client object to communicate with your currently running MongoDB instance
'''
client = MongoClient()
print(client)
#>>>MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
'''
to provide a custom host and port, you can use the following code:
1.client = MongoClient(host="localhost", port=27017)
or
2.client = MongoClient("mongodb://localhost:27017")
'''
#define which database you want to use
'''
 you can use the dot notation just like you did in the mongo shell:
 '''
db = client.pydb1
'''
also use dictionary-style access 
if the name of the database isn’t a valid Python identifier:
db = client["pydb1"]
'''
print(db)
#>>>Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'pydb1')
print(db.name)
''' prints database name'''
#>>>pydb1
'''
use dictionaries to create documents
'''
user1={
    "username":"durga",
    "role":"Teacher"
}
'''
specify which collection you want to use
'''
users = db.user #db.cllection-name
print(users)
#>>>Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'pydb1'), 'user')
'''
insert documents into user by calling .insert_one() 
'''
one_result = users.insert_one(user1)
print("insrted the doc")
#>>>insrted the doc
print(one_result)
#>>><pymongo.results.InsertOneResult object at 0x00000099BB23B208>
print(f"User1: {one_result.inserted_id}")
#>>>User1: 60a6676724966527325584ac
'''
use .insert_many() to insert them in one go
'''
user2={
    "username":"A.Ram",
    "role":"student"
}
user3={
    "username":"A.Shyam",
    "role":"student"
}
user4={
    "username":"B.Gani",
    "role":"teacher"
}
user5={
    "username":"B.Kiran",
    "role":"teacher"
}
many_result =users.insert_many([user2, user3,user4,user5])
print(f"Multiple users: {many_result.inserted_ids}")
#>>>Multiple users: [ObjectId('60a6676724966527325584ad'), ObjectId('60a6676724966527325584ae'), ObjectId('60a6676724966527325584af'), ObjectId('60a6676724966527325584b0')]
#close connection => close the connection by calling .close() on the MongoClient instance
client.close()