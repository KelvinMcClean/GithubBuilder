from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Analysis.PullGitData import reset_wd
from Analyse_Projects.Get_Project_Data import *
from Analyse_People.Get_People_Data import *
from Analyse_Projects.Dates import *

def main():
    reset_wd()
    doc = get_unanalysed_projects()

    for x in doc:
        ght_id = x['ghtorrent_id']
        owner = x['owner']
        name = x['name']
        # Pull project commit info
        # Pull project commit comments
        # Add information onto users
        contributers = list()

        commits = get_commit_info(ght_id)
        put_commits_in_dates(commits, x)
        if len(commits) > 0:
            for commit in commits:
                handle_user_exists(commit['committer_id'], ght_id)

                comments = get_commit_comments(commit['id'])
                if comments != 0:
                    for row in comments:
                        user_id = row['user_id']
                        timestamp = row['created_at']
                        handle_user_exists(user_id, ght_id)
                        if user_id not in contributers:
                            contributers.append(user_id)
                        put_user_in_date(user_id, timestamp)

        # Get pull request info
        # Get pull request comments
        # Add information onto users

        pull_requests = get_pull_request_info(ght_id)
        put_pull_requests_in_dates(pull_requests, x)

        if len(pull_requests) > 0:
            for pull_request in pull_requests:
                comments = get_pull_request_comments(pull_request['id'])
                if comments != 0:
                    for row in comments:
                        user_id = row['user_id']
                        timestamp = row['created_at']
                        handle_user_exists(user_id, ght_id)
                        if user_id not in contributers:
                            contributers.append(user_id)
                        put_user_in_date(user_id,timestamp)

        # Pull project issue info
        # Pull project issue comments
        # Add information onto users

        issues = get_issue_info(owner, name)
        put_issues_in_dates(issues, x)

        if len(issues) > 0:
            for issue in issues:
                comments = get_issue_comments(owner, name, issue['number'])
                if comments != 0:
                    for row in comments:
                        user_id = row['user_id']
                        timestamp = row['created_at']
                        handle_user_exists(user_id, ght_id)
                        if user_id not in contributers:
                            contributers.append(user_id)
                        put_user_in_date(user_id, timestamp)
        local_dates = get_dates()
        x['dates'] = [d['id_tag'] for d in local_dates]

        insert_into_dates(local_dates)
        clear_dates()



if __name__ == "__main__":
    main()
