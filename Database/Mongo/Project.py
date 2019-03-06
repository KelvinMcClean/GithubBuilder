class Project:

    def __init__(self, project_info):
        self.ghtorrent_id = project_info['id']                #GHT
        self.name = project_info['name']                                #GHT
        self.owner = project_info['owner']                              #GHT
        self.space = project_info['space']                              #Code
        self.size = project_info['size']                                #API
        self.LOC = project_info['LOC']                                  #Code
        self.contributor_count = project_info['contributor_count']      #GHT
        self.contributors = project_info['contributors']                #GHT
        self.dates = project_info['dates']                              #GHT?/API/Code
        self.issues = project_info['issues']                            #
        self.created_on = project_info['year']                          #GHT
        self.deleted = project_info['deleted']                         #GHT
