from MainDirectory.DatabaseInfo import *
from Database import *
from MainDirectory.PushData import insert_into_projects_list
import requests

def get_person(person):

    response = requests.get('https://api.github.com/users/{0}'.format(person), auth=(key_user, key_auth))
    username = response.json()['login']

    type_of_org = response.json()['type']

    year_created = int(response.json()['created_at'][:4])
    hireable = 0
    if response.json()['hireable']:
        hireable = 1
    public_repos = response.json()['public_repos']
    followers = response.json()['followers']
    following = response.json()['following']
    github_id = response.json()['id']

    a_person = User(github_id, username, year_created, type_of_org, 0, hireable, 0, public_repos, 0, 0,
                    followers, following)
    return a_person


def get_person_projects(person, page):
    repos_list = requests.get('https://api.github.com/users/{0}/repos?page={1}'.format(person, page),
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
            year = int(repo['created_at'][:4])
            year_updated = int(repo['updated_at'][:4])
            programming_language = repo['language']
            github_id = repo['id']

            project = Project(id, name, owner, space, size, LOC, contributor_count, contributors, dates, issues, year)
            project_id = insert_into_projects_list(vars(project))

