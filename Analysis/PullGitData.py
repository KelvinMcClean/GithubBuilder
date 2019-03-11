import subprocess as s
import os
import Analysis.FileInfo
import requests

wd = "D:/repos"


def reset_wd():
    global wd
    wd = "D:/repos"
    os.chdir(wd)


def clone_project(owner, project):
    reset_wd()
    cmd = "git clone https://www.github.com/{0}/{1} {0}/{1}".format(owner, project)
    s.call(cmd, shell=True)


def get_project_on_date(owner, project, date):
    global wd
    wd = "D:/repos/{0}/{1}".format(owner, project)
    os.chdir(wd)

    cmd = "git rev-list -1 --before=\"{0}\" master".format(date)
    output = bytes(s.check_output(cmd, shell=True)).decode("utf8")
    cmd = "git checkout {0}".format(output)
    s.call(cmd, shell=True)


def examine_project(owner, project, date):

    text = Analysis.FileInfo.get_file_text(owner, project, date)
    f = open("sonar-project.properties", "w+")
    f.write(text)
    f.close()

    cmd = "sonar-scanner"
    s.call(cmd, shell=True)


def get_metrics(owner, project):
    payload = {'metricKeys': 'ncloc, complexity', 'component': '{0}::{1}'.format(owner, project)}
    result = requests.get("http://localhost:9000/api/measures/component", params=payload)
    data = result.json()
    data_dict = dict()
    for json_var in data['component']['measures']:
        if json_var['metric'] == 'ncloc':
            data_dict["ncloc"] = json_var['value']
        elif json_var['metric'] == 'complexity':
            data_dict["complexity"] = 'complexity'
    return data_dict


# USE API call to check if it's there. If it's not, remove it?
