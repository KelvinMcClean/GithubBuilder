class Dates:

    def __init__(self, ghtorrent_id, name, LOC, churn, contributor_count, commits, contributors):
        self.ghtorrent_id = ghtorrent_id            #GHT
        self.name = name                            #GHT
        self.LOC = LOC                              #Code
        self.churn = churn                          #Code
        self.contributor_count = contributor_count  #GHT
        self.commits = commits                      #GHT/ Mongo
        self.contributors = contributors            #GHT/ Mongo