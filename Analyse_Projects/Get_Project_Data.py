import pymongo
import Analyse_People.Get_People_Data as gp
from Database.GHTorrent.Connection import *
from MainDirectory.PushData import *
import MainDirectory.GetData as gd

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["github_builder_db"]
user_col = mydb["Users"]
proj_col = mydb["Projects"]
dates_col = mydb["Dates"]

def get_unanalysed_projects():
    query = {"analysed": False}
    doc = proj_col.find(query)
    return doc


def update_mongo_project_dates(project, date_key):
    project_info = proj_col.find_one({"ghtorrent_id":project['ghtorrent_id']})
    project_info['dates'].append(date_key)
    proj_col.update_one({'ghtorrent_id': project['ghtorrent_id']}, {"$set":{'dates':project_info['dates']}})


def insert_date_mongo(date_to_update):
    dates_col.insert_one(date_to_update)


def update_date_mongo(date_to_update, metrics):
    dates_col.update_one({"id_tag":date_to_update['id_tag']},{"$set":{"metrics":metrics}})


def get_mongo_date_from_key(date_key):
    query = {"id_tag":date_key}
    return dates_col.find_one(query)


def get_date_key_exists(date_key):
    query = {"id_tag":date_key}
    if dates_col.find_one(query) is not None:
        return 1
    else:
        return 0


def update_contributors(project, collaborators):
    try:
        proj_col.update_one({"_id":project['_id']},{"$set":{'collaborators':collaborators}})
    except:
        print("Error when updating project collaborators")

def get_distinct_pr_commentators(ght_id):
    return get_ghtorrent_distinct_pr_commentators(ght_id)


def get_distinct_issue_commentators(ght_id):
    return get_ghtorrent_distinct_issue_commentators(ght_id)


def get_distinct_commit_commentators(ght_id):
    return get_ghtorrent_distinct_commit_commentators(ght_id)


def handle_user_exists(user_id, ght_id):
    if gp.get_user_by_id(user_id) is not None:
        return
    else:
        person = gd.get_person(user_id)
        insert_into_people_list(vars(person))
        insert_into_people()
        return


def get_commit_info(ght_id):
    result = -1
    commits = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_project_commits(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            commits.extend(result)

    if len(commits) == 0:
        return 0
    else:
        return commits


def get_issue_info(ght_id):
    result = -1
    issues = list()
    dict_issues = list()
    loop = 0
    result = get_ghtorrent_project_issues(ght_id)
    if result != 0:
        loop = loop + 100
        for issue in result:
            new_issue = dict()
            new_issue['id'] = issue[0]
            new_issue['created_at'] = issue[6]
            new_issue['closed_at'] = get_ghtorrent_issue_closed_on(issue[0])
            dict_issues.append(new_issue)
        issues.extend(result)

    if len(dict_issues) == 0:
        return 0
    else:
        return dict_issues




def get_commit_comments(ght_id):
    result = -1
    comments = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_commit_comments(ght_id)
        return result
    if len(comments) == 0:
        return 0
    else:
        return comments


def get_issue_comments(ght_id):
    result = -1
    issue_comments = list()
    loop = 0
    result = get_ghtorrent_issue_comments(ght_id)
    if result != 0:
        issue_comments.extend(result)

    if len(issue_comments) == 0:
        return 0
    else:
        return issue_comments


def get_pull_request_comments(ght_id):
    result = -1
    pull_requests = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_pull_request_comments(ght_id)
        pull_requests.extend(result)

    if len(pull_requests) == 0:
        return 0
    else:
        return pull_requests

