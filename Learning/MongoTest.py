import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = my_client["mydatabase"]
my_col = my_db["customers"]

my_query = { "address": "Park Lane 38" }
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

print("==================")

my_query = { "address": { "$gt": "S" } }
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

print("==================")

my_query = { "address": { "$regex": "^S" } }
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

print("==================")

my_doc = my_col.find().sort("name")
for x in my_doc:
    print(x)

print("==================")

my_query = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}

my_col.update_one(my_query, new_values)

for x in my_col.find():
    print(x)
