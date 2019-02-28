from MainDirectory.DatabaseInfo import *
from Database import *

import requests
import pymongo


def insert_into_people():
    users_collection.insert_many(people)
    people.clear()


def insert_into_projects():
    projects_collection.insert_many(projects)
    projects.clear()


def get_person(person):

    response = requests.get('https://api.github.com/users/{0}'.format(person), auth=(key_user, key_auth))
    username = response.json()['login']

    type_of_org = response.json()['type']

    year_created = response.json()['created_at'][:4]
    hireable = "0"
    if response.json()['hireable']:
        hireable = "1"
    public_repos = str(response.json()['public_repos'])
    followers = str(response.json()['followers'])
    following = str(response.json()['following'])
    github_id = str(response.json()['id'])

    a_person = User(github_id, username, year_created, type_of_org, 0, hireable, 0, public_repos, 0, 0,
                    followers, following)
    return a_person


def insert_into_people_list(person):
    people.append(person)
    return people.index(person)


def insert_into_projects_list(project):
    projects.append(project)
    return projects.index(project)

def main():
    print("Load up file for results...")
    print(db_loc)

    username = 'reergymerej'
    person = get_person(username)

    person_id = insert_into_people_list(vars(person))

    page = 0

    num_repos = int(person.projects)

    print(person_id)
    while (page * 30) < num_repos:
        page = page + 1

        repos_list = requests.get('https://api.github.com/users/{0}/repos?page={1}'.format(username, page),
                                  auth=(key_user, key_auth))

        for i in range(len(repos_list.json())):
            repo = repos_list.json()[i]
            url = repo['url']
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
                stargazer_count = repo['stargazers_count']
                watchers_count = repo['watchers_count']
                forks_count = repo['forks']
                year = repo['created_at'][:4]
                year_updated = repo['updated_at'][:4]
                programming_language = repo['language']
                github_id = repo['id']

                project = Project(id,name,owner,space,size,LOC,contributor_count,contributors,dates,issues, year)
                project_id = insert_into_projects_list(vars(project))

                """
                project = (person_id, name, stargazer_count, watchers_count, forks_count, year_created, year_updated,
                           programming_language, github_id)
                insert_into_projects(conn, project)
                """

    insert_into_people()
    insert_into_projects()
    """print('Number of projects: {0}'.format(response.json()['total_count']))
    #print('Number of repos: {0}'.format(response.json()['public_repos']))
    #print(response.json()[0]['id'])
    #print(len(response.json()))
    if conn is not None:
        create_table(conn, sql_create_users_table)

        conn.close()

    else:
        print("Error! Cannot create database Connection")

    print("See where to start...")

    print("Load command to go to GH and get data")

    print("Count API calls")

    print("Process call and data received. Process.")
"""


if __name__ == "__main__":
    people = []
    projects = []
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = my_client["github_builder_db"]
    users_collection = db["Users"]
    projects_collection = db["Projects"]

    main()
