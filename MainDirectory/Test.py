
database = "D:/Experiment/Data.db"

db_loc = "Database location: " + database
auth_loc = "D:/Experiment/auth/auth.txt"
user_loc = "D:/Experiment/auth/username.txt"
f = open(auth_loc, "r")
key_auth = f.read()
f.close()
f = open(user_loc, "r")
key_user = f.read()
f.close()
sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                       id integer PRIMARY KEY,
                                       username text NOT NULL,
                                       year_created integer,
                                       hireable integer,
                                       public_repos integer,
                                       owned_repos integer,
                                       followers integer,
                                       following integer,
                                       location text,
                                       github_id integer NOT NULL
                                   ); """

sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    owner_id integer NOT NULL,
                                    name text NOT NULL,
                                    stargazer_count integer,
                                    watchers_count integer,
                                    forks_count integer,
                                    year_created integer,
                                    year_updated integer,
                                    programming_language text,
                                    github_id integer NOT NULL
                                    
                                );"""


