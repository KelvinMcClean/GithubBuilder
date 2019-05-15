from Analyse_People.Get_People_Data import get_user_by_id
from Analyse_People.Collaborators import *
from Analyse_Projects.Get_Project_Data import *
from Analysis.Timestamp import *
dates = dict()


def get_date_from_time(timestamp, ght_id):
    corrected_timestamp = get_corrected_timestamp(timestamp)
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
        date = get_date_from_time(commit[5], ght_id)
        date['commits'] = date['commits'] + 1

        ids = get_distinct_commit_commentators(commit[0])
        commentators = [get_user_by_id(u_id) for u_id in ids]
        for i in range(0, len(commentators)):
            for j in range(0, len(commentators)):
                if i != j:
                    add_connection(commentators[i], commentators[j], date)

        user = get_user_by_id(commit[3])
        author = get_user_by_id(commit[2])
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



def put_issues_in_dates(issues, project):
    ght_id = project['ghtorrent_id']

    for issue in issues:
        date = get_date_from_time(issue['created_at'], ght_id)
        date['issues'] = date['issues'] + 1

        ids = get_distinct_issue_commentators(issue['id'])
        commentators = [get_user_by_id(u_id) for u_id in ids]
        for i in range(0, len(commentators)):
            for j in range(0, len(commentators)):
                if i != j:
                    add_connection(commentators[i], commentators[j], date)

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
