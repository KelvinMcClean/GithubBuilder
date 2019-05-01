import pymongo
from Database.GHTorrent.Connection import *
from MainDirectory.PushData import *


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["github_builder_db"]
mycol = mydb["Users"]
proj_col = mydb["Projects"]


def get_unanalysed_projects():
    query = {"analysed": False}
    doc = proj_col.find(query)
    return doc


def get_commit_info(ght_id):
    result = -1
    commits = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_project_commits(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            commits.extend(result)

    if len(commits == 0):
        return 0
    else:
        return commits

def get_issue_info(ght_id):
    result = -1
    issues = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_project_issues(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            for issue in result:
                issue['closed_at'] = get_ghtorrent_issue_closed_on(issue['id'])
            issues.extend(result)

    if len(issues == 0):
        return 0
    else:
        return issues


def get_pull_request_info(ght_id):
    result = -1
    pull_requests = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_project_pull_requests(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            pull_requests.extend(result)

    if len(pull_requests == 0):
        return 0
    else:
        return pull_requests


def get_commit_comments(ght_id):
    result = -1
    comments = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_commit_comments(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            comments.extend(result)

    if len(comments == 0):
        return 0
    else:
        return comments


def get_issue_comments(ght_id):
    result = -1
    issues = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_issue_comments(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            issues.extend(result)

    if len(issues == 0):
        return 0
    else:
        return issues


def get_pull_request_comments(ght_id):
    result = -1
    pull_requests = list()
    loop = 0
    while result != 0:
        result = get_ghtorrent_pull_request_comments(ght_id, loop, 100)
        if result != 0:
            loop = loop + 100
            pull_requests.extend(result)

    if len(pull_requests == 0):
        return 0
    else:
        return pull_requests

