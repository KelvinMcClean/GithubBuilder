from MainDirectory.GetData import *
from MainDirectory.PushData import *





def main():
    print("Load up file for results...")
    print(db_loc)

    username = 'reergymerej'
    person = get_person(username)

    insert_into_people_list(vars(person))
    ght_id = person.ghtorrent_id
    get_person_projects(ght_id)

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
