# GithubBuilder


## Setup
You need to have an account set up with Github and GHTorrent, a mongo db set up, and a sonarqube server running.

### GHTorrent
Set up account as following instructions on main GHTorrent website.
Run the SQL server on using 'ssh -L 3306:web.ghtorrent.org:3306 ghtorrent@web.ghtorrent.org', sign in as necessary

### Github account
You can modify where your uname and authorisation are stored, but by default they need to be placed in files 'username.txt' and 'auth.txt' in D://Experiment/auth.
These are used to pull down the projects' code through the Github API.

### Mongo db
Run mongo server on localhost:27017

### Sonarqube
Sonarqube scanner needs to be set up through to work via the command line. As such, it needs to be added to the system PATH.
The sonarqube server needs to be run as well, so the results of the scanner can be saved, and then analysed later.

### Packages
Need to install the following packages:
- PyMySQL
- certifi
- chardet
- idna
- mysqlclient
- numpy
- pip
- pymongo
- python-dateutil
- pytz
- requests
- setuptools
- six
- urllib3

## Usage Instructions
On the first pass, run MainDirectory/Main.py. This will seed the dataset with 100 users and their projects.
From their, run Analyse_People/Main.py and Analyse_Projects/Main.py as necessary to get relevent data. Analyse_People will take a subset of the unanalysed people in the dataset and build up personal and project relationships, while Analyse_Projects will examine the people who worked on a subset of unanalysed projects.
