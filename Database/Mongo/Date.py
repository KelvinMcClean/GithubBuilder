class Date:

    def __init__(self, date_info):
        self.ghtorrent_id = date_info.ghtorrent_id            #GHT
        self.name = date_info.name                            #GHT
        self.LOC = date_info.LOC                              #Code
        self.churn = date_info.churn                          #Code
        self.contributor_count = date_info.contributor_count  #GHT
        self.commits = date_info.commits                      #GHT/ Mongo
        self.contributors = date_info.contributors            #GHT/ Mongo
