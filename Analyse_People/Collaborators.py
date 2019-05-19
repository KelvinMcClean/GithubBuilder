from Analyse_People.Get_People_Data import update_collaboration
list_to_update = list()


def add_group_connection(group, date):
    # Get this to work. Not being added to the model.
    for i in range(0, len(group)):
        for j in range(0, len(group)):
            if i != j:
                add_connection(group[i], group[j], date)


def add_connection(person_a, person_b, date):
    if 'collaborators' not in person_a.keys():
        person_a['collaborators'] = dict()
    if 'collaborators' not in person_b.keys():
        person_b['collaborators'] = dict()

    if str(person_b['ghtorrent_id']) in person_a['collaborators'].keys():
        person_a['collaborators'][str(person_b['ghtorrent_id'])]['strength'] +=1
        if date['id_tag'] in person_a['collaborators'][str(person_b['ghtorrent_id'])].keys():
            person_a['collaborators'][str(person_b['ghtorrent_id'])][date['id_tag']] +=1
        else:
            person_a['collaborators'][str(person_b['ghtorrent_id'])][date['id_tag']] = 1
    else:
        person_a['collaborators'][str(person_b['ghtorrent_id'])] = dict()
        person_a['collaborators'][str(person_b['ghtorrent_id'])][date['id_tag']] = 1
        person_a['collaborators'][str(person_b['ghtorrent_id'])]['strength'] =1


    if str(person_a['ghtorrent_id']) in person_b['collaborators'].keys():
        person_b['collaborators'][str(person_a['ghtorrent_id'])]['strength'] +=1
        if date['id_tag'] in person_b['collaborators'][str(person_a['ghtorrent_id'])].keys():
            person_b['collaborators'][str(person_a['ghtorrent_id'])][date['id_tag']] +=1
        else:
            person_b['collaborators'][str(person_a['ghtorrent_id'])][date['id_tag']] = 1
    else:
        person_b['collaborators'][str(person_a['ghtorrent_id'])] = dict()
        person_b['collaborators'][str(person_a['ghtorrent_id'])][date['id_tag']] = 1
        person_b['collaborators'][str(person_a['ghtorrent_id'])]['strength'] =1

    update_collaboration(person_a, person_b)
