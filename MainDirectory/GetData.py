from Database import *
from MainDirectory.PushData import insert_into_projects_list
from Database.GHTorrent.Connection import *
from MainDirectory.PushData import projects
from MainDirectory.PushData import people
import datetime
import Analysis.PullGitData as pgd


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


def analyse_projects(dates):
    for project in projects:
        deleted = project['deleted']
        if not deleted:
            p_name = project['name']
            p_owner = project['owner']
            owner = min(elem['login'] for elem in people if elem['ghtorrent_id'] == p_owner)
            pgd.clone_project(owner, p_name)

    for date in dates:
        date_value = datetime.datetime.strptime(date, '%Y-%m-%d')
        for project in projects:
            deleted = project['deleted']
            if not deleted:
                p_name = project['name']
                p_owner = project['owner']
                owner = min(elem['login'] for elem in people if elem['ghtorrent_id'] == p_owner)
                date_created = project['created_on']

                if date_created < date_value:
                    pgd.get_project_on_date(owner, p_name, date)
                    pgd.examine_project(owner, p_name, date)
                    metrics = pgd.get_metrics(owner, p_name)
                    metrics['date'] = date
                    project['dates'].append(metrics)

        for project in projects:
            deleted = project['deleted']
            if not deleted:
                p_name = project['name']
                p_owner = project['owner']
                owner = min(elem['login'] for elem in people if elem['ghtorrent_id'] == p_owner)

                metrics = pgd.get_metrics(owner, p_name)
                metrics['date'] = date
                project['dates'].append(metrics)

