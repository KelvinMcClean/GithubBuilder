import subprocess as s
import os
import Analysis.FileInfo
import requests
import time

wd = "D:/repos"


def reset_wd():
    global wd
    wd = "D:/repos"
    os.chdir(wd)


def clone_project(owner, project):
    reset_wd()
    cmd = "git clone https://github.com/{0}/{1}.git/ {0}/{1}".format(owner, project)
    s.call(cmd, shell=True)


def get_project_on_date(owner, project, date):
    try:
        global wd
        wd = "D:/repos/{0}/{1}".format(owner, project)
        os.chdir(wd)

        cmd = "git rev-list -1 --before=\"{0}\" master".format(date)
        output = bytes(s.check_output(cmd, shell=True)).decode("utf8")
        cmd = "git checkout {0}".format(output)
        s.call(cmd, shell=True)
    except:
        print("Code is breaking at dl ")

def examine_project(owner, project, date):

    text = Analysis.FileInfo.get_file_text(owner, project, date)
    f = open("sonar-project.properties", "w+")
    f.write(text)
    f.close()

    cmd = "sonar-scanner"
    s.call(cmd, shell=True, stdout=s.DEVNULL)


def get_metrics(owner, project):
    print("getting metrics")
    payload = {'metricKeys': 'ncloc, complexity', 'component': '{0}::{1}'.format(owner, project)}
    result = requests.get("http://localhost:9000/api/measures/component", params=payload)
    data = result.json()
    data_dict = dict()
    if result.status_code != 200 or len(data['component']['measures']) == 0:
        return -1
    for json_var in data['component']['measures']:
        if json_var['metric'] == 'ncloc':
            data_dict["ncloc"] = json_var['value']
        elif json_var['metric'] == 'complexity':
            data_dict["complexity"] = json_var['value']
        else:
            return -1
    return data_dict


# USE API call to check if it's there. If it's not, remove it?
