import pymongo

people = list()
projects = list()

people_ids = list()
project_ids = list()

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = my_client["github_builder_db"]
users_collection = db["Users"]
projects_collection = db["Projects"]
dates_collection = db["Dates"]

def insert_into_dates(dates):
    if len(dates) == 0:
        return
    elif "Dates" in db.list_collection_names():
        dates_collection.insert_many(dates)
    else:
        if len(dates) > 1:
            dates_collection.insert_one(dates.pop())
            dates_collection.insert_many(dates)
        else:
            dates_collection.insert_one(dates.pop())

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
        if len(people) > 1:
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


