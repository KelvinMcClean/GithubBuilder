import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="ght", db="ghtorrent")
cur = db.cursor()


def get_ghtorrent_user(login):
    cur.execute("SELECT id, login, company, created_at, "
                "type, fake, deleted, country_code, "
                "state, city FROM users WHERE login='{0}'".format(login))
    return cur.fetchone()


def get_ghtorrent_user_orgs(ghtorrent_id):
    response = cur.execute("SELECT org_id, created_at from organization_members WHERE user_id='{0}'".format(ghtorrent_id))
    if response == 0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_user_projects_from_login(login):
    response = cur.execute("SELECT p.id, p.url, p.name, p.language, p.created_at, p.updated_at, p.deleted "
                           "FROM projects as p "
                           "INNER JOIN users ON users.id=p.owner_id "
                           "WHERE users.login='{0}' AND p.forked_from IS NULL;".format(login))
    if response ==0:
        return response
    else:
        return cur.fetchall()


def get_ghtorrent_user_projects(ghtorrent_id):
    response = cur.execute("SELECT p.id, p.url, p.name, p.language, p.created_at, p.updated_at, p.deleted "
                           "FROM projects as p"
                           "WHERE p.owner_id='{0}' AND p.forked_from IS NULL;".format(ghtorrent_id))
    if response ==0:
        return response
    else:
        return cur.fetchall()
