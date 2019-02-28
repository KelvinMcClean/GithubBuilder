class User:

    def __init__(self, ghtorrent_id, login, date_created, p_type, orgs, company, hirable, spaces, projects, stars, collaborators,
                 followers, following):
        self.ghtorrent_id = ghtorrent_id
        self.login = login
        self.date_created = date_created
        self.type = p_type
        self.orgs = orgs
        self.company = company
        self.hirable = hirable
        self.spaces = spaces
        self.projects = projects
        self.stars = stars
        self.collaborators = collaborators
        self.followers = followers
        self.following = following

