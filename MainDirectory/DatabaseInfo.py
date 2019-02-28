
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
