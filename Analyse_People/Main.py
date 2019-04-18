from Analyse_People.Get_People_Data import *
from Analyse_People.Update import *
from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Analysis.PullGitData import reset_wd


def main():
    reset_wd()
    doc = get_unanalysed_people()
    list_of_elements = list()
    list_of_new_people_to_add = list()
    for x in doc:
        ght_id = x['ghtorrent_id']
        #get_person_projects(ght_id)
        if x['type'] == "USR":
            orgs = get_orgs(x)
            if orgs != 0:
                x['orgs'] = orgs
                for org in x['orgs']:
                    list_of_new_people_to_add.append(org)
        elif x['type'] == "ORG":
            members = get_org_members(x)
            if members == 0:
                print("Nothing todo")
            else:
                for mem in members:
                    list_of_new_people_to_add.append(mem)

        list_of_elements.append(x)

    #insert_into_projects()

    for org in list_of_new_people_to_add:
        if not checkdb(org[0]) and not check_person_list(org[0]):
            person = get_person(org[0])

            insert_into_people_list(vars(person))

    insert_into_people()
    push_updates(list_of_elements)


if __name__ == "__main__":
    main()
