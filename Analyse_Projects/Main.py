from Analysis.PullGitData import reset_wd
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
        contributors = list()

        commits = get_commit_info(ght_id)
        put_commits_in_dates(commits, x)
        if len(commits) > 0:
            for commit in commits:
                handle_user_exists(commit[3], ght_id)

                comments = get_commit_comments(commit[0])
                if comments != 0:
                    for row in comments:
                        user_id = row[2]
                        timestamp = row[7]
                        handle_user_exists(user_id, ght_id)
                        if user_id not in contributors:
                            contributors.append(user_id)
                        put_user_in_date(user_id, timestamp)

        issues = get_issue_info(owner, name)
        put_issues_in_dates(issues, x)

        if len(issues) > 0:
            for issue in issues:
                comments = get_issue_comments(issue[0])
                if comments != 0:
                    for row in comments:
                        user_id = row[1]
                        timestamp = row[3]
                        handle_user_exists(user_id, ght_id)
                        if user_id not in contributors:
                            contributors.append(user_id)
                        put_user_in_date(user_id, timestamp)

        local_dates = get_dates()
        x['dates'] = [d['id_tag'] for d in local_dates]

        insert_into_dates(local_dates)
        clear_dates()
        local_dates.clear()
        contributors.clear()


if __name__ == "__main__":
    main()
