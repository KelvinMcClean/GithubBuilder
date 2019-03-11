
def get_file_text(owner, project, date):

    text = "sonar.projectKey = {0}::{1}\r\n" \
           "sonar.projectName={0}::{1}\r\n" \
           "sonar.projectVersion={2}\r\n" \
           "sonar.sources=\"\\\"".format(owner, project, date)
    return text
