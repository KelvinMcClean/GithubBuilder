from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Analysis.PullGitData import reset_wd
from Analyse_Projects.Get_Project_Data import *

def main():
    reset_wd()
    doc = get_unanalysed_projects()

    for x in doc:
        ght_id = x['ghtorrent_id']

        # Pull project commit info
        # Pull project commit comments
        # Add information onto users

        commits = get_commit_info(ght_id)
        if len(commits) > 0:
            for commit in commits:
                comments = get_commit_comments(commit['id'])

        # Get pull request info
        # Get pull request comments
        # Add information onto users

        pull_requests = get_pull_request_info(ght_id)
        if len(pull_requests) > 0:
            for pull_request in pull_requests:
                comments = get_pull_request_comments(pull_request['id'])

        # Pull project issue info
        # Pull project issue comments
        # Add information onto users

        issues = get_issue_info(ght_id)
        if len(issues) > 0:
            for issue in issues:
                comments = get_issue_comments(issue['id'])




if __name__ == "__main__":
    main()
