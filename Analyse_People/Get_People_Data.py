import pymongo
from Database.GHTorrent.Connection import *
from MainDirectory.PushData import *


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["github_builder_db"]
mycol = mydb["Users"]
proj_col = mydb["Projects"]


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


def checkprojdb(ght_id):
    if proj_col.find_one({"ghtorrent_id": ght_id}) is not None:
        return 1
    else:
        return 0

def check_person_list(ght_id):
    return ght_id in people_ids

def check_proj_list(ght_id):
    return ght_id in project_ids

def get_projects_by_member(ght_id):
    result = -1
    membership_list = list()
    loop = 0
    while result!=0:
        result=get_ghtorrent_projects_by_member(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            for project in result:
                membership_list.append(project)

    if len(membership_list == 0):
        return 0
    else:
        return membership_list


def get_projects_committed_to(ght_id):
    result = -1
    committed_list = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_projects_by_comments(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            for project in result:
                committed_list.append(project)

    if len(committed_list == 0):
        return 0
    else:
        return committed_list
