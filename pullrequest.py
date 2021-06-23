#!/usr/bin/env python
from github import Github
from local_settings import *
# PullRequestの操作

token = MY_OAUTH_TOKEN

g = Github(token)
