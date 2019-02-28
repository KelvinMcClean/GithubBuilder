import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="ght", db="ghtorrent")
cur = db.cursor()


def get_ghtorrent_user(login):
    cur.execute("SELECT id, login, company, created_at, "
                "type, fake, deleted, country_code, "
                "state, city FROM users WHERE login='{0}'".format(login))
    return cur.fetchone()


def get_ghtorrent_is_in_org(ghtorrent_id):
    response = cur.execute("SELECT org_id, created_at from organization_members WHERE user_id='{0}'".format(ghtorrent_id))
    if response == 0:
        return response
    else:
        return cur.fetchall()
