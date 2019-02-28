class Issue:

    def __init__(self, ghtorrent_id, name, resolved, contributors, opened_time, closed_time):
        self.ghtorrent_id = ghtorrent_id
        self.name = name
        self.resolved = resolved
        self.contributors = contributors
        self.opened_time = opened_time
        self.closed_time = closed_time