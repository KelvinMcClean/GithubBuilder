import pymongo

people = list()
projects = list()

people_ids = list()
project_ids = list()

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = my_client["github_builder_db"]
users_collection = db["Users"]
projects_collection = db["Projects"]


def insert_into_people_list(person):
    people.append(person)
    people_ids.append(person['ghtorrent_id'])
    return people.index(person)


def insert_into_projects_list(project):
    projects.append(project)
    project_ids.append(project['ghtorrent_id'])
    return projects.index(project)


def insert_into_people():
    if len(people) == 0:
        return

    elif "Users" in db.list_collection_names():
        users_collection.insert_many(people)
        people.clear()
        people_ids.clear()

    else:
        if len(people) > 2:
            users_collection.insert_one(people.pop())
            users_collection.insert_many(people)
            people.clear()
            people_ids.clear()

        elif len(people) == 1:
            users_collection.insert_one(people.pop())
            people_ids.clear()


def insert_into_projects():
    if len(projects) == 0:
        return

    elif "Projects" in db.list_collection_names():
        projects_collection.insert_many(projects)
        projects.clear()
        project_ids.clear()

    else:
        if len(projects) > 1:
            projects_collection.insert_one(projects.pop())
            projects_collection.insert_many(projects)
            projects.clear()
            project_ids.clear()

        elif len(projects) == 1:
            projects_collection.insert_one(projects.pop())
            project_ids.clear()


