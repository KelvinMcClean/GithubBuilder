from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Analysis.PullGitData import reset_wd
import subprocess as s

def main():
    reset_wd()
    username = 'reergymerej'
    person = get_person(username)

    insert_into_people_list(vars(person))
    ght_id = person.ghtorrent_id
    get_person_projects(ght_id)

    this_file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = this_file_path+"/../Analysis/dates"
    with open(file_path) as fp:
        dates = fp.readlines()
    dates = [x[:-1] for x in dates]
    analyse_projects(dates)
    insert_into_people()
    insert_into_projects()
    result = 1  # requests.post("http://localhost:9000/api/projects/bulk_delete", auth=("admin", "admin"))
    if result.status_code == 204:
        print("Deleted projects from sonarqube")
    os.chdir("D://")
    cmd = "rmdir /S /Q repos"
    s.call(cmd, shell=True)
    cmd = "mkdir repos"
    s.call(cmd, shell=True)
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
