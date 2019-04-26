import MySQLdb
import os
path = os.path.dirname(__file__)
db_host_loc = os.path.join(path, "connection_config")
f = open(db_host_loc, "r")
host = f.read()
f.close()

db = MySQLdb.connect(host, user="ght", db="ghtorrent")
cur = db.cursor()


def get_ghtorrent_user(login):
    cur.execute(" SELECT id, login, company, created_at, "
                " type, fake, deleted, country_code "
                " FROM users WHERE login='{0}'".format(login))
    return cur.fetchone()


def get_ghtorrent_user_by_ghtid(ght_id):
    cur.execute(" SELECT id, login, company, created_at, "
                " type, fake, deleted, country_code "
                " FROM users WHERE id='{0}'".format(ght_id))
    return cur.fetchone()

def get_ghtorrent_user_orgs(ghtorrent_id):
    response = cur.execute("SELECT org_id, created_at from organization_members WHERE user_id='{0}'"
                           .format(ghtorrent_id))
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_user_projects_from_login(login):
    response = cur.execute("SELECT p.id, p.url, p.name, p.language, p.created_at, p.updated_at, p.deleted "
                           "FROM projects as p "
                           "INNER JOIN users ON users.id=p.owner_id "
                           "WHERE users.login='{0}' AND p.forked_from IS NULL LIMIT 10;".format(login))
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_user_projects(ghtorrent_id):
    query = "SELECT p.id, p.url, p.name, p.language, p.created_at, p.updated_at, p.deleted " \
            "FROM projects as p WHERE p.owner_id='{0}' AND p.forked_from IS NULL;".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_user_orgs(ghtorrent_id):
    query = "SELECT u.id, u.login, u.company, u.created_at, u.type," \
            "u.fake, u.deleted, u.country_code, o.created_at FROM organization_members as o " \
            "INNER JOIN users as u ON o.org_id=u.id " \
            "WHERE o.user_id ='{0}'".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_user_org_members(ghtorrent_id):
    query = "SELECT u.id, u.login, u.company, u.created_at, u.type, u.fake, u.deleted, u.country_code," \
            "o.created_at FROM organization_members as o " \
            "INNER JOIN users as u ON org_id=u.id " \
            "WHERE o.org_id ='{0}'".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_projects_by_member(ghtorrent_id, start_limit, number):
    query = "SELECT p.id, p.owner_id, p.name, p.language, p.created_at, p.updated_at, p.deleted FROM projects as p \
            INNER JOIN project_members as pm ON pm.repo_id = p.id WHERE pm.user_id = '{0}' LIMIT {1}, {2};".format(ghtorrent_id, start_limit, number)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_projects_by_comments(ghtorrent_id, start_limit, number):
    query = "SELECT DISTINCT p.id, p.owner_id, p.name, p.created_at, p.deleted " \
            "FROM commits as c INNER JOIN projects as p ON c.project_id = p.id " \
            "WHERE c.committer_id = '18030' AND p.forked_from IS NULL " \
            "LIMIT {0}, {1};".format(ghtorrent_id, start_limit, number)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_project_commits(ghtorrent_id, start_limit, number):
    query = "SELECT * FROM commits WHERE project_id = '{0}' LIMIT {1}, {2};".format(ghtorrent_id, start_limit, number);
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_project_pull_requests(ghtorrent_id, start_limit, number):
    query = "SELECT * FROM pull_requests WHERE head_repo_id = '{0}' LIMIT {1}, {2};".format(ghtorrent_id, start_limit, number);
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_project_issues(ghtorrent_id, start_limit, number):
    query = "SELECT * FROM issues WHERE repo_id = '{0}' LIMIT {1}, {2};".format(ghtorrent_id, start_limit, number);
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_commit_comments(ghtorrent_id):
    query = "SELECT * FROM commit_commets WHERE commit_id='{0}';".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_pull_request_comments(ghtorrent_id):
    query = "SELECT * FROM pull_request_comments WHERE pull_request_id='{0}';".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_issue_comments(ghtorrent_id):
    query = "SELECT * FROM issue_comments WHERE issue_id='{0}';".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()
