import pymongo
from Database.GHTorrent.Connection import *
from MainDirectory.PushData import *


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["github_builder_db"]
mycol = mydb["Users"]


def get_unanalysed_people():
    query = {"analysed": False}
    doc = mycol.find(query)
    return doc


def get_all_people():
    doc = mycol.find()
    return doc


def get_orgs(user):
    return get_ghtorrent_user_orgs(user['ghtorrent_id'])


def get_org_members(user):
    return get_ghtorrent_user_org_members(user['ghtorrent_id'])


def checkdb(ght_id):
    if mycol.find_one({"ghtorrent_id": ght_id}) is not None:
        return 1
    else:
        return 0


def check_person_list(ght_id):
    return ght_id in people_ids
