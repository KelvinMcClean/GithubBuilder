class Issue:

    def __init__(self, p_id, name, resolved, contributors, opened_time, closed_time):
        self.p_id = p_id
        self.name = name
        self.resolved = resolved
        self.contributors = contributors
        self.opened_time = opened_time
        self.closed_time = closed_time