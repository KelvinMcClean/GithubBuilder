
database = "D:/Experiment/Data.db"

db_loc = "Database location: " + database
sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                       id integer PRIMARY KEY,
                                       username text NOT NULL,
                                       year_created integer,
                                       hireable integer,
                                       public_repos integer,
                                       followers integer,
                                       following integer,
                                       location text
                                   ); """

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""


