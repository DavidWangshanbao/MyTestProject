#!/usr/bin/env python
# coding=utf-8
import os
from fabric.api import task, env, cd, run,hosts
from fabric.context_managers import settings
from fabric.operations import sudo
from fabtools import require


env.port = "22"
env.user = "dnet"

# NOTE: 需要清理的ELK的地址
@hosts([ '172.17.11.141'])
@task
def test_sudo():
    """
    test fabric sudo
    :return:
    """
    with settings(sudo_user="root"):
        sudo("whoami")
        sudo("cp  /hdapp/test2/envfile  /hdapp/test2/envfile_bak")



