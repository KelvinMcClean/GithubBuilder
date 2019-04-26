from Analyse_People.Get_People_Data import *
from Analyse_People.Update import *
from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Analysis.PullGitData import reset_wd
from Analyse_People.Process import *

def main():
    reset_wd()
    doc = get_unanalysed_people()
    list_of_elements = list()
    list_of_new_people_to_add = list()
    list_of_projects_to_add = list()
    for x in doc:
        ght_id = x['ghtorrent_id']
        get_person_projects(ght_id)
        if x['type'] == "USR":

            orgs = get_orgs(x)
            if orgs != 0:
                x['orgs'] = orgs
                for org in x['orgs']:
                    person = create_person_from_search(org)
                    list_of_new_people_to_add.append(person)

            projects_member_of = get_projects_by_member(ght_id)
            if projects_member_of != 0:
                for project in projects_member_of:
                    project_oop = create_project_from_search(project)
                    list_of_projects_to_add.append(project_oop)

            projects_committed_to = get_projects_committed_to(ght_id)
            if projects_committed_to != 0:
                for project in projects_committed_to:
                    project_oop = create_project_from_search(project)
                    list_of_projects_to_add.append(project_oop)

        elif x['type'] == "ORG":

            members = get_org_members(x)
            if members != 0:
               for mem in members:
                    person = create_person_from_search(mem)
                    list_of_new_people_to_add.append(person)

        list_of_elements.append(x)

    insert_into_projects()

    for usr in list_of_new_people_to_add:
        if not checkdb(usr[0]) and not check_person_list(usr[0]):
            person = get_person(usr[0])

            insert_into_people_list(vars(person))

    for prj in list_of_projects_to_add:
        if not checkprojdb(prj['id']) and not check_proj_list(prj['id']):
            insert_into_projects_list(project)

    insert_into_people()
    insert_into_projects()
    push_updates(list_of_elements)


if __name__ == "__main__":
    main()
