from MainDirectory.DatabaseInfo import *
from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Database import *

import requests
import pymongo




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
        get_person_projects(username, page)

    insert_into_people()
    insert_into_projects()
    """
    print('Number of projects: {0}'.format(response.json()['total_count']))
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
