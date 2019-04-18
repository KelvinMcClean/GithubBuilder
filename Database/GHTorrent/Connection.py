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
    query = "SELECT org_id, users.login, o.created_at FROM organization_members as o " \
            "INNER JOIN users ON org_id=users.id " \
            "WHERE user_id ='{0}'".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()

def get_ghtorrent_user_org_members(ghtorrent_id):
    query = "SELECT o.user_id, users.login, o.created_at FROM organization_members as o " \
            "INNER JOIN users ON org_id=users.id " \
            "WHERE o.org_id ='{0}'".format(ghtorrent_id)
    response = cur.execute(query)
    if response == 0:
        return response
    else:
        return cur.fetchall()

