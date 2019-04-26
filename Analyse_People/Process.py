from Database.Mongo.User import *
from Database.Mongo.Project import *

def create_person_from_search(resp):
    person = dict()
    person['ght'] = resp[0]
    person['login'] = resp[1]
    person['company'] = resp[2]
    person['date_created'] = resp[3]
    person['type'] = resp[4]
    person['deleted'] = resp[6]
    person['country'] = resp[7]
    a_person = User(person)
    return a_person

def create_project_from_search(resp):
    response_project = dict()
    response_project['id'] = resp[0]
    response_project['owner'] = resp[1]
    response_project['name'] = resp[2]
    response_project['space'] = 0
    response_project['contributor_count'] = 0
    response_project['contributors'] = 0
    response_project['dates'] = list()
    response_project['issues'] = 0
    response_project['year'] = resp[3]
    response_project['deleted'] = resp[4]

    project = Project(response_project)
    return project
