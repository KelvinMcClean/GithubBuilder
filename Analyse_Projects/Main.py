
from Analysis.PullGitData import reset_wd
from Analyse_Projects.Dates import *
import Analyse_Projects.AnalyseProjectQuality

# Look at whether I'm uploading changes
# Changes include: project changes, date changes, people changes
# Add data to download and assess quality of code.
# Run a run of it tonight...

def main():
    reset_wd()
    doc = get_unanalysed_projects().limit(500)
    projects_to_analyse = list()
    for x in doc:
        projects_to_analyse.append(x)
    for x in projects_to_analyse:
        print("New doc")
        ght_id = x['ghtorrent_id']
        owner = x['owner']
        name = x['name']
        # Pull project commit info
        # Pull project commit comments
        # Add information onto users
        contributors = list()
        print("\t commits")

        commits = get_commit_info(ght_id)
        print("\t got info")
        if commits != 0 and len(commits) > 0:
            put_commits_in_dates(commits, x)
            for commit in commits:
                print("\t\tHandle commit")
                handle_user_exists(commit[3], ght_id)
                print("\t\tHandle comments")
                comments = get_commit_comments(commit[0])
                if comments != 0:
                    for row in comments:
                        print("\t\t\tROW in comments")
                        user_id = row[2]
                        timestamp = row[7]
                        print("\t\t\tHandle user exists")

                        handle_user_exists(user_id, ght_id)
                        print("\t\t\tAdd to contribs")

                        if user_id not in contributors:
                            contributors.append(user_id)
                        print("\t\t\tAdd to date")

                        put_user_in_date(ght_id,user_id, timestamp)
        print("\t issues")

        issues = get_issue_info(ght_id)

        if issues != 0 and len(issues) > 0:
            put_issues_in_dates(issues, x)
            for issue in issues:
                comments = get_issue_comments(issue['id'])
                if comments != 0:
                    for row in comments:
                        user_id = row[1]
                        timestamp = row[3]
                        handle_user_exists(user_id, ght_id)
                        if user_id not in contributors:
                            contributors.append(user_id)
                        put_user_in_date(ght_id, user_id, timestamp)

        local_dates = get_dates()
        dates = list(local_dates.keys())
        x['dates'] = dates
        proj_col.update_one({'ghtorrent_id':x['ghtorrent_id']}, {'$set':{'dates':x['dates']}})
        insert_into_dates(local_dates)
        clear_dates()
        local_dates.clear()

        update_contributors(x,contributors)

        contributors.clear()
    print("Analyse projects")

    Analyse_Projects.AnalyseProjectQuality.quality(projects_to_analyse)


if __name__ == "__main__":
    main()
