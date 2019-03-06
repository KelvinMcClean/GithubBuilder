from MainDirectory.DatabaseInfo import *
from Database import *
from MainDirectory.PushData import insert_into_projects_list
import requests
from Database.GHTorrent.Connection import *


def get_person(person):


    # a_person = User(github_id, login, year_created, type_of_org, 0, hireable, 0, public_repos, 0, 0,
    #                 followers, following, ghtorrent_id)

    response = get_ghtorrent_user(person)
    response_person = dict()
    response_person['login'] = response[1]

    response_person['type'] = response[4]

    response_person['date_created'] = response[3]
    response_person['hirable'] = 0
    # if response.json()['hireable']:
    #     hireable = 1
    response_person['projects'] = 0
    response_person['followers'] = 0
    response_person['following'] = 0
    response_person['orgs'] = 0
    response_person['ght'] = response[0]
    response_person['company'] = response[2]
    response_person['spaces'] = 0
    response_person['stars'] = 0
    response_person['collaborators'] = 0
    response_person['fake'] = response[5]
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
        response_project['size'] = 0
        response_project['LOC'] = 0
        response_project['contributor_count'] = 0
        response_project['contributors'] = 0
        response_project['dates'] = 0
        response_project['issues'] = 0
        response_project['year'] = item[4]
        response_project['deleted'] = item[6]

        project = Project(response_project)
        insert_into_projects_list(vars(project))


def get_followers():
    pass
