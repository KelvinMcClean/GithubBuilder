class User:

    def __init__(self, p_id, name, age, p_type, member_of, hirable, spaces, projects, stars, collaborators,
                 followers, following):
        self.p_id = p_id
        self.name = name
        self.age = age
        self.type = p_type
        self.member_of = member_of
        self.hirable = hirable
        self.spaces = spaces
        self.projects = projects
        self.stars = stars
        self.collaborators = collaborators
        self.followers = followers
        self.following = following
