from Analyse_People.Get_People_Data import get_user_by_id
from Analyse_People.Collaborators import *
dates = dict()


def get_date_from_time(timestamp, ght_id):
    corrected_timestamp = timestamp
    date = None
    if corrected_timestamp in dates.keys():
        date = dates[corrected_timestamp]
    else:

        date = dict()
        date['id_tag'] = "gh{0}ts{1}".format(ght_id, timestamp)
        date['timestamp'] = corrected_timestamp
        date['commits'] = 0
        date['pull_requests'] = 0
        date['issues'] = 0
        date['issues_resolved'] = 0
        date['contributors'] = dict()
        dates[corrected_timestamp] = date
    return date


def put_commits_in_dates(commits, project):
    ght_id = project['ghtorrent_id']
    for commit in commits:
        date = get_date_from_time(commit['created_at'], ght_id)
        date['commits'] = date['commits'] + 1

        user = get_user_by_id(commit['committer_id'])
        author = get_user_by_id(commit['author_id'])
        add_connection(user, author, date)
        if "projects" not in user.keys():
            user['projects'] = dict()

        if ght_id in user['projects'].keys():
            user['projects'][ght_id]['commits'] += 1
            if date['id_tag'] in user['projects'][ght_id]['dates']:
                user['projects'][ght_id]['dates']['commits'] += 1
            else:
                newDate = {'id_tag':date['id_tag'], 'commits':1}
            user['projects'][ght_id]['dates'][date['id_tag']] = newDate
        else:
            project_to_add = {'id':ght_id, 'commits': 1,
                              'dates':{date['id_tag']:{'id_tag': date['id_tag'], 'commits': 1}}}
            user['projects'][ght_id] = project_to_add


def put_pull_requests_in_dates(pull_requests, project):
    ght_id = project['ghtorrent_id']
    for pull_request in pull_requests:
        date = get_date_from_time(pull_request['created_at'], ght_id)
        date['pull_requests'] = date['pull_requests'] + 1


def put_issues_in_dates(issues, project):
    ght_id = project['ghtorrent_id']

    for issue in issues:
        date = get_date_from_time(issue['created_at'], ght_id)
        date['issues'] = date['issues'] + 1
        if issue['closed_at'] is not None:
            date_closed = get_date_from_time(issue['closed_at'], ght_id)
            date_closed['issues_resolved'] = date_closed['issues_resolved'] + 1


def put_user_in_date(user_id, timestamp):
    date = get_date_from_time(timestamp)
    users = date['contributors']
    if user_id in users.keys():
        users[user_id] = users[user_id] + 1
    else:
        users[user_id] = 1

    date['contributors'] = users


def get_dates():
    return dates


def clear_dates():
    dates.clear()
