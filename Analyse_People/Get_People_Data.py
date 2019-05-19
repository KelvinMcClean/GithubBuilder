import pymongo
import MainDirectory.GetData as gd
from Database.GHTorrent.Connection import *
from MainDirectory.PushData import *

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["github_builder_db"]
user_col = mydb["Users"]
proj_col = mydb["Projects"]
dates_col = mydb["Dates"]


def update_collaboration(person_a, person_b):
    try:
        user_col.update_one({'ghtorrent_id': person_a['ghtorrent_id']},{'$set': {'collaborators':person_a['collaborators']}})
        user_col.update_one({'ghtorrent_id': person_b['ghtorrent_id']},{'$set': {'collaborators':person_b['collaborators']}})
    except:
        print("Error in pymongo update")


def get_unanalysed_people():
    query = {"analysed": False}
    doc = user_col.find(query)
    return doc


def get_all_people():
    doc = user_col.find()
    return doc


def get_orgs(user):
    return get_ghtorrent_user_orgs(user['ghtorrent_id'])


def get_org_members(user):
    return get_ghtorrent_user_org_members(user['ghtorrent_id'])


def checkdb(ght_id):
    if user_col.find_one({"ghtorrent_id": ght_id}) is not None:
        return 1
    else:
        return 0


def checkprojdb(ght_id):
    if proj_col.find_one({"ghtorrent_id": ght_id}) is not None:
        return 1
    else:
        return 0


def get_user_by_id(ght_id):
    user = user_col.find_one({"ghtorrent_id": ght_id})
    if user is None:
        user = gd.get_person(ght_id)
        user_col.insert_one(vars(user))
        user = user_col.find_one({"ghtorrent_id": ght_id})
    return user

def check_person_list(ght_id):
    return ght_id in people_ids


def check_proj_list(ght_id):
    return ght_id in project_ids


def get_projects_by_member(ght_id):
    result = -1
    membership_list = list()
    loop = 0
    while result!=0:
        result=get_ghtorrent_projects_by_member(ght_id, loop, 1000)
        if result != 0:
            loop = loop + 1000
            for project in result:
                membership_list.append(project)

    if len(membership_list) == 0:
        return 0
    else:
        return membership_list


def get_projects_committed_to(ght_id):
    result = -1
    committed_list = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_projects_by_comments(ght_id, loop, 1000)
        if result != 0:
            loop = loop + 1000
            for project in result:
                committed_list.append(project)

    if len(committed_list) == 0:
        return 0
    else:
        return committed_list


def get_person_followers(ght_id):
    result = -1
    followers_list = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_user_followers(ght_id, loop, 1000)
        if result !=0:
            loop = loop + 1000
            for person in result:
                followers_list.append(person)
    if len(followers_list) == 0:
        return 0
    else:
        return followers_list

def get_person_following(ght_id):
    result = -1
    following_list = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_user_following(ght_id, loop, 1000)
        if result != 0:
            loop = loop + 1000
            for person in result:
                following_list.append(person)
    if len(following_list) == 0:
        return 0
    else:
        return following_list


def get_person_stars(ght_id):
    result = -1
    stars_list = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_user_stars(ght_id, loop, 1000)
        if result != 0:
            loop = loop + 1000
            for star in result:
                stars_list.append(star)
    if len(stars_list) == 0:
        return 0
    else:
        return stars_list
