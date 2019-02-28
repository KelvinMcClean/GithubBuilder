import pymongo

people = []
projects = []

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = my_client["github_builder_db"]
users_collection = db["Users"]
projects_collection = db["Projects"]


def insert_into_people_list(person):
    people.append(person)
    return people.index(person)


def insert_into_projects_list(project):
    projects.append(project)
    return projects.index(project)

def insert_into_people():
    users_collection.insert_many(people)
    people.clear()


def insert_into_projects():
    projects_collection.insert_many(projects)
    projects.clear()

