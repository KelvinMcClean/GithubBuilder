class Issue:

    def __init__(self, ghtorrent_id, issue_type, resolved, contributors, opened_time, closed_time):
        self.ghtorrent_id = ghtorrent_id    #GHT
        self.issue_type = issue_type        #GHT
        self.resolved = resolved            #GHT
        self.contributors = contributors    #GHT/ API
        self.opened_time = opened_time      #API
        self.closed_time = closed_time      #API
