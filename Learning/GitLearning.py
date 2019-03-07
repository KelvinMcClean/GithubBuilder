import subprocess as s
import os
import Learning.FileInfo
import requests
import time

print(s.check_output("dir D:", shell=True))
wd = "D:/repos"
os.chdir(wd)
owner = "KelvinMcClean"
proj = "GithubBuilder"
cmd = "git clone https://www.github.com/{0}/{1}".format(owner, proj)

# s.call(cmd)

wd = "D:/repos/{0}".format(proj)
os.chdir(wd)

cmd = "git rev-list -1 --before=\"2019-02-08\" master"
output = bytes(s.check_output(cmd, shell=True)).decode("utf8")
print(output)
cmd = "git checkout {0}".format(output)
s.call(cmd, shell=True)

text = Learning.FileInfo.get_file_text(owner, proj, "2019-02-06")
print(text)
f = open("sonar-project.properties", "w+")
f.write(text)
f.close()

cmd = "sonar-scanner"
s.call(cmd, shell=True)
payload = {'metricKeys': 'ncloc, complexity', 'component': '{0}::{1}'.format(owner, proj)}
result = requests.get("http://localhost:9000/api/measures/component", params=payload)
data = result.json()
print(data['component']['measures'][0]['value'])
wd = "D:/repos"
os.chdir(wd)
# cmd = "rmdir /S /Q GithubBuilder"
# s.call(cmd, shell=True)
