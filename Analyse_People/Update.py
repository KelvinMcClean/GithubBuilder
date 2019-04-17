import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["github_builder_db"]
mycol = mydb["Users"]


def push_updates(updated_doc):
    print(updated_doc)
    for x in updated_doc:
        x['analysed'] = True
        x_id = x['_id']

        query = {"_id": x_id}
        newvalues = {"$set": {'analysed': True}}
        if 'orgs' in x:
            newvalues["$set"]['orgs'] = x['orgs']
        mycol.update_one(query, newvalues)
        print("updated values")

