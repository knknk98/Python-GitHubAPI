#!/usr/bin/env python
from github import Github
from local_settings import *
# PullRequestの操作

token = MY_OAUTH_TOKEN
g = Github(token)
repo = g.get_repo(REPO_NAME)

pulls = repo.get_pulls(state='open', sort='created', base='main')
for pr in pulls:
    print(pr.title)
