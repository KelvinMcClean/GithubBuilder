class User:

    def __init__(self, ghtorrent_id, login, date_created, p_type, orgs, company, hirable, spaces, projects, stars, collaborators,
                 followers, following):
        self.ghtorrent_id = ghtorrent_id        #GHT
        self.login = login                      #GHT
        self.date_created = date_created        #GHT
        self.type = p_type                      #GHT
        self.orgs = orgs                        #GHT
        self.company = company                  #GHT
        self.hirable = hirable                  #Mongo
        self.spaces = spaces                    #Code
        self.projects = projects                #GHT
        self.stars = stars                      #GHT
        self.collaborators = collaborators      #GHT/ Code
        self.followers = followers              #GHT
        self.following = following              #GHT

