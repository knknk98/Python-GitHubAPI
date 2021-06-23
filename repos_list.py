#!/usr/bin/env python
from github import Github
from local_settings import *
# 自分のリポジトリ一覧を取得

token = MY_OAUTH_TOKEN
g = Github(token)

print("🦀自分のリポジトリ一覧を取得🦀")
print("[名前,最終更新日時,デフォルトブランチ,openしてるissueの数]")
for repo in g.get_user().get_repos(type='owner'):
    print(repo.name, repo.updated_at, repo.default_branch, repo.open_issues_count)

print("🦀Contributors一覧取得🦀")
for repo in g.get_user().get_repos(type='owner'):
    print([repo.name])
    for contributer in repo.get_contributors():
        print(contributer.login)
