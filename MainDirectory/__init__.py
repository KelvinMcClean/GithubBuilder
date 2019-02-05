from GithubBuilder.MainDirectory.Test import *
import sqlite3
from sqlite3 import Error
import requests


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
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


def main():
    print("Load up file for results...")
    print(db_loc)

    #conn = create_connection(database)
    #response = requests.get('https://api.github.com/search/repositories?q=stars%3A%3E0&sort=stars')

    #print('Number of projects: {0}'.format(response.json()['total_count']))

    response = requests.get('https://api.github.com/users/reergymerej')
    print('Number of repos: {0}'.format(response.json()['public_repos']))
    person = response.json()['login']
    response = requests.get('https://api.github.com/users/{0}/repos' .format(person))
    print(response.json()[0]['id'])
    """if conn is not None:
        create_table(conn, sql_create_users_table)

        conn.close()

    else:
        print("Error! Cannot create database Connection")
"""
    print("See where to start...")

    print("Load command to go to GH and get data")

    print("Count API calls")

    print("Process call and data received. Process.")


if __name__ == "__main__":
    main()
