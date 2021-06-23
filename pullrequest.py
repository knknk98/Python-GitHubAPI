#!/usr/bin/env python
from github import Github
from local_settings import *
import random
from datetime import datetime, timedelta
# PullRequestの操作

token = MY_OAUTH_TOKEN
g = Github(token)
repo = g.get_repo(REPO_NAME)

# レビュアーをランダムで1人決める
members = list(repo.get_collaborators())
randomized_member = random.choice(members)
print(randomized_member.login)

# プルリクにランダムでレビュアー/assignees設定
pulls = repo.get_pulls(state='open', sort='created', base='main')
for pr in pulls:
    pr.create_review_request([randomized_member.login])
    pr.add_to_assignees(randomized_member)

# m分以上更新されていないプルリク取得
# Get time now
now = datetime.now()
m = 10
for p in pulls:
    if now - p.updated_at > timedelta(minutes=m):
        print(p.title + 'がしばらく更新されていません')
