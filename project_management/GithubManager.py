from datetime import datetime, timedelta
from github import Github, Repository

def getGroupProjectRepo() -> Repository:
    githubAPIToken = "55ea860df525188ae65ac4546072fbf2f29ab386"
    g = Github(githubAPIToken)
    return g.get_user("JesseGuerrero").get_repo("temporary_name")


def countCommitsByDate(repository : Repository, member) -> int:
    currentDate = datetime.fromisocalendar(2021, 1, 1)
    endDate = datetime.today()

    count = 0
    while (currentDate <= endDate):
        currentDate = currentDate + timedelta(days=1)
        if repository.get_commits(since=currentDate - timedelta(days=1), until=currentDate, author=member).totalCount > 0:
            count += 1
    return count