# GithubBuilder


## Usage instructions
You need to have an account set up with Github and GHTorrent, a mongo db set up, and a sonarqube server running.

###GHTorrent
Set up account as following instructions on main GHTorrent website.
Run the SQL server on using 'ssh -L 3306:web.ghtorrent.org:3306 ghtorrent@web.ghtorrent.org', sign in as necessary

###Github account
You can modify where your uname and authorisation are stored, but by default they need to be placed in files 'username.txt' and 'auth.txt' in D://Experiment/auth.
These are used to pull down the projects' code through the Github API.

###Mongo db
Run mongo server on localhost:27017

###Sonarqube
Sonarqube scanner needs to be set up through to work via the command line. As such, it needs to be added to the system PATH.
The sonarqube server needs to be run as well, so the results of the scanner can be saved, and then analysed later.
