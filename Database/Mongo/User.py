class User:

    def __init__(self, user_info):
        self.ghtorrent_id = user_info['ght']
        self.login = user_info['login']                       # GHT
        self.date_created = user_info['date_created']         # GHT
        self.type = user_info['type']                         # GHT
        self.company = user_info['company']                   # GHT
        self.deleted = user_info['deleted']                   # GHT

        self.analysed = False                                 # Own Metric


