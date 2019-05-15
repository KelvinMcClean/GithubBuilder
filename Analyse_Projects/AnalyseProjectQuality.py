from MainDirectory.GetData import *
import subprocess as s


def quality():
    this_file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = this_file_path + "/../Analysis/dates"
    with open(file_path) as fp:
        dates = fp.readlines()
    dates = [x[:-1] for x in dates]
    analyse_projects(dates)
    result = requests.post("http://localhost:9000/api/projects/bulk_delete", auth=("admin", "admin"))
    if result.status_code == 204:
        print("Deleted projects from sonarqube")
    os.chdir("D://")
    cmd = "rmdir /S /Q repos"
    s.call(cmd, shell=True)
    cmd = "mkdir repos"
    s.call(cmd, shell=True)


if __name__ == "__main__":
    main()
