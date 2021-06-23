#!/usr/bin/env python
from github import Github
from local_settings import *
# Issuesの操作

token = MY_OAUTH_TOKEN
g = Github(token)
repo = g.get_repo(REPO_NAME)

# 未解決かつbugのラベルがついたissueを取得して最新更新日が古い順で取得
issue_list = repo.get_issues(
    state='open', labels=['bug'], direction='asc', sort='created')

for _issue in issue_list:
    print('issue name: #{:<4} {}'.format(_issue.number, _issue.title))
