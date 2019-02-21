from GithubBuilder.MainDirectory.DatabaseInfo import *
import sqlite3
from sqlite3 import Error
import requests
import json


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_into_people(conn, person):
    try:
        sql = '''INSERT INTO users 
                    (username, type, year_created, hireable, public_repos, followers, following, github_id) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        c = conn.cursor()
        c.execute(sql, person)
        conn.commit()

        return c.lastrowid
    except Error as e:
        print(e)


def insert_into_projects(conn, project):
    try:
        sql = '''INSERT INTO projects 
                    (owner_id, name, stargazer_count, watchers_count, forks_count, year_created, year_updated, 
                    programming_language, github_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        c = conn.cursor()
        c.execute(sql, project)
        conn.commit()

        return c.lastrowid
    except Error as e:
        print(e)

def main():
    print("Load up file for results...")
    print(db_loc)

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_projects_table)

        response = requests.get('https://api.github.com/users/reergymerej', auth=(key_user, key_auth))
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

        person = (username, type_of_org, year_created, hireable, public_repos, followers, following, github_id)

        person_id = insert_into_people(conn, person)

        page = 0

        num_repos = response.json()['public_repos']

        print(person_id)
        while (page * 30) < num_repos:
            page = page + 1

            repos_list = requests.get('https://api.github.com/users/{0}/repos?page={1}'.format(username, page),
                                      auth=(key_user, key_auth))

            for i in range(len(repos_list.json())):
                repo = repos_list.json()[i]
                url = repo['url']
                project_data = requests.get(url, auth=(key_user, key_auth))
                is_fork = project_data.json()['fork']
                if not is_fork:

                    name = project_data.json()['name']
                    stargazer_count = project_data.json()['stargazers_count']
                    watchers_count = project_data.json()['watchers_count']
                    forks_count = project_data.json()['forks']
                    year_created = project_data.json()['created_at'][:4]
                    year_updated = project_data.json()['updated_at'][:4]
                    programming_language = project_data.json()['language']
                    github_id = project_data.json()['id']
                    project = (person_id, name, stargazer_count, watchers_count, forks_count, year_created, year_updated,
                               programming_language, github_id)
                    insert_into_projects(conn, project)


        conn.close()
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
    main()
