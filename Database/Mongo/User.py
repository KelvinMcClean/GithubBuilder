class User:

    def __init__(self, user_info):
        self.ghtorrent_id = user_info['ght']
        self.login = user_info['login']                       # GHT
        self.date_created = user_info['date_created']         # GHT
        self.type = user_info['type']                       # GHT
        self.orgs = user_info['orgs']                         # GHT
        self.company = user_info['company']                   # GHT
        self.hirable = user_info['hirable']                   # Mongo
        self.spaces = user_info['spaces']                     # Code
        self.projects = user_info['projects']                 # GHT
        self.stars = user_info['stars']                       # GHT
        self.collaborators = user_info['collaborators']       # GHT/ Code
        self.followers = user_info['followers']               # GHT
        self.following = user_info['following']               # GHT

