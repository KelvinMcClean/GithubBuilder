from Database import *
from Analyse_Projects.Get_Project_Data import *
from MainDirectory.PushData import people
import Analysis.PullGitData as pgd
import requests
from MainDirectory.DatabaseInfo import *
import pandas as pd


def get_person(ght_id):


    # a_person = User(github_id, login, year_created, type_of_org, 0, hireable, 0, public_repos, 0, 0,
    #                 followers, following, ghtorrent_id)

    response = get_ghtorrent_user_by_ghtid(ght_id)
    response_person = dict()
    response_person['ght'] = response[0]
    response_person['login'] = response[1]
    response_person['date_created'] = response[3]
    response_person['type'] = response[4]
    response_person['company'] = response[2]
    response_person['deleted'] = response[6]
    response_person['country'] = response[7]

    a_person = User(response_person)
    return a_person


def get_person_projects(ght_id):

    response = get_ghtorrent_user_projects(ght_id)

    if response == 0:
        return

    for item in response:
        response_project = dict()
        response_project['id'] = item[0]
        response_project['name'] = item[2]
        response_project['owner'] = ght_id
        response_project['space'] = 0
        response_project['contributor_count'] = 0
        response_project['contributors'] = 0
        response_project['dates'] = list()
        response_project['issues'] = 0
        response_project['year'] = item[4]
        response_project['deleted'] = item[6]

        project = Project(response_project)
        insert_into_projects_list(vars(project))


def get_followers():
    pass


def analyse_projects(projects_to_analyse, dates):
    for project in projects_to_analyse:
        deleted = project['deleted']
        if not deleted:
            p_name = project['name']
            p_owner = project['owner']
            owner = user_col.find_one({'ghtorrent_id':p_owner})
            owner_login = owner['login']
            if requests.get("https://api.github.com/repos/{0}/{1}".format(owner_login, p_name),
                            auth=(key_user, key_auth)).status_code == 200:
                pgd.clone_project(owner_login, p_name)
            else:
                project['deleted'] = True

    for date in dates:
        date_value = pd.to_datetime(date)
        for project in projects_to_analyse:
            print("1")
            deleted = project['deleted']
            if not deleted:
                p_name = project['name']
                p_owner = project['owner']
                p_id = project['ghtorrent_id']
                owner_oop = user_col.find_one({'ghtorrent_id': p_owner})
                owner = owner_oop['login']
                date_created = project['created_on']

                if date_created < date_value:
                    print("tester")
                    pgd.get_project_on_date(owner, p_name, date)
                    pgd.examine_project(owner, p_name, date)
                    metrics = -1
                    loop = 0
                    while metrics == -1 and loop < 10:
                        loop += 1
                        metrics = pgd.get_metrics(owner, p_name)

                    if loop <= 10:
                        date_key = "gh{0}ts{1}".format(p_id, date_value)  # Get date key
                        if date_key_exists(date_key):
                            date_to_update = get_date_from_key(date_key)
                            update_date(date_to_update, metrics)

                        else:
                            date_to_update = dict()
                            date_to_update['metrics'] = metrics
                            insert_date(date_to_update)
                        update_project_dates(project, date_key)


    for project in projects_to_analyse:
        print("3")
        set_analysed(project)


def date_key_exists(date_key):
    return get_date_key_exists(date_key)

def get_date_from_key(date_key):
    return get_mongo_date_from_key(date_key)

def update_date(date_to_update, metrics):
    update_date_mongo(date_to_update, metrics)

def insert_date(date_to_update):
    insert_date_mongo(date_to_update)

def update_project_dates(project, date_key):
    update_mongo_project_dates(project, date_key)

def set_analysed(project):
    proj_col.update_one({"ghtorrent_id":project['ghtorrent_id']}, {"$set":{"analysed":True}})

