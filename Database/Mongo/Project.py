class Project:

    def __init__(self, ghtorrent_id, name, owner, space, size, LOC, contributor_count, contributors, dates, issues,
                 created_on, updated_on):
        self.ghtorrent_id = ghtorrent_id                #GHT
        self.name = name                                #GHT
        self.owner = owner                              #GHT
        self.space = space                              #Code
        self.size = size                                #API
        self.LOC = LOC                                  #Code
        self.contributor_count = contributor_count      #GHT
        self.contributors = contributors                #GHT
        self.dates = dates                              #GHT?/API/Code
        self.issues = issues                            #
        self.created_on = created_on                    #GHT
        self.updated_on = updated_on                    #GHT
