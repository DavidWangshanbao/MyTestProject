#!/usr/bin/python
# -*- coding:UTF-8 -*-
from __future__ import unicode_literals, print_function
from docker.harborclient import HarborClient
import json
client = HarborClient("harborka.qianfan123.com", "admin", "XJOvN1GhQQk8eyUc", "https")
client.login()
repo_name = "jcrm/jcrm-server-card"
repo_name_tags = client.get_repository_tags(repo_name)
repo_name_tags = json.dumps(repo_name_tags)
print(repo_name_tags)