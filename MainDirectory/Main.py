from MainDirectory.GetData import *
from MainDirectory.PushData import *
from Analysis.PullGitData import reset_wd


def main():
    reset_wd()

    this_file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = this_file_path + "\\ids"
    with open(file_path) as fp:
        ids = fp.readlines()
    id_data = [x[:-1] for x in ids]
    for ght_id in id_data:
        person = get_person(ght_id)

        insert_into_people_list(vars(person))

    insert_into_people()


if __name__ == "__main__":
    main()
