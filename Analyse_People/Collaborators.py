from Analyse_People.Get_People_Data import update_collaboration
list_to_update = list()


def add_connection(person_a, person_b, date):
    if 'collaborators' not in person_a.keys():
        person_a['collaborators'] = dict()
    if 'collaborators' not in person_b.keys():
        person_b['collaborators'] = dict()

    if person_b['id'] in person_a['collaborators'].keys():
        person_a['collaborators'][person_b['id']]['strength'] +=1
        if date['id_tag'] in person_a['collaborators'][person_b['id']].keys():
            person_a['collaborators'][person_b['id']][date['id_tag']] +=1
        else:
            person_a['collaborators'][person_b['id']][date['id_tag']] = 1

    if person_a['id'] in person_b['collaborators'].keys():
        person_b['collaborators'][person_a['id']]['strength'] +=1
        if date['id_tag'] in person_b['collaborators'][person_a['id']].keys():
            person_b['collaborators'][person_a['id']][date['id_tag']] +=1
        else:
            person_b['collaborators'][person_a['id']][date['id_tag']] = 1

    update_collaboration(person_a, person_b)
