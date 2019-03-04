from MainDirectory.DatabaseInfo import *
from Database import *
from MainDirectory.PushData import insert_into_projects_list
import requests
from Database.GHTorrent.Connection import *


def get_person(person):


    # a_person = User(github_id, login, year_created, type_of_org, 0, hireable, 0, public_repos, 0, 0,
    #                 followers, following, ghtorrent_id)

    response = get_ghtorrent_user(person)
    response_person = {}
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


def get_person_projects(person, page):
    repos_list = requests.get('https://api.github.com/users/{0}/repos?page={1}'.format(person, page),
                              auth=(key_user, key_auth))

    for i in range(len(repos_list.json())):
        repo = repos_list.json()[i]
        is_fork = repo['fork']
        if not is_fork:
            id = repo['id']
            name = repo['name']
            owner = repo['owner']['id']
            space = 0
            size = repo['size']
            LOC = 0
            contributor_count = 0
            contributors = 0
            dates = 0
            issues = 0
            year = int(repo['created_at'][:4])

            project = Project(id, name, owner, space, size, LOC, contributor_count, contributors, dates, issues, year)
            insert_into_projects_list(vars(project))


def get_followers():
    pass
