import pymongo
from Database.GHTorrent.Connection import *

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

