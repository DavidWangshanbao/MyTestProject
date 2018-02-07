# coding=utf-8
from __future__ import unicode_literals, print_function
import os

from utils import load_yaml
from toolz import get_in

##################
#  Constants
##################
RDS_TIMEOUT = 180

__cfg = None


def get_db_connection(subsystem='dmm',alias='dmm'):
    """
    获取MySQL数据库连接
    docs： http://pymysql.readthedocs.io/en/latest/
    :param subsystem: e.g.: dmm,dbo
    :return:
    """
    import pymysql
    host = get_config([subsystem, 'db_connection',alias, 'host'])
    db = get_config([subsystem, 'db_connection',alias, 'db'])
    password = get_config([subsystem, 'db_connection',alias, 'password'])
    user = get_config([subsystem, 'db_connection',alias, 'user'])
    charset = get_config([subsystem, 'db_connection',alias, 'charset'])

    return pymysql.connect(host=host, db=db, password=password, user=user,
                           charset=charset,
                           connect_timeout=RDS_TIMEOUT, read_timeout=RDS_TIMEOUT,
                           write_timeout=RDS_TIMEOUT)


def get_active_profile():
    return os.environ.get('DNET_PROFILE', 'integration_test')


def get_baseurl(subsystem='dmm'):
    return get_config([subsystem, 'base_url'])


def load_config():
    global __cfg
    if __cfg is None:
        basedir = os.path.dirname(__file__)
        __cfg = load_yaml(os.path.join(basedir, 'config.yaml'))


def get_cfg_object():
    global __cfg
    return __cfg


def get_config(path_list=None, force_reload=False):
    if path_list is None:
        raise ValueError("unknow key")
    elif not isinstance(path_list, list):
        raise ValueError("path_list should be a list object")

    global __cfg
    if force_reload:
        __cfg = None
    load_config()

    return get_in([get_active_profile()] + path_list, __cfg)


if __name__ == '__main__':
    assert get_config(['dmm', 'base_url']) == 'https://dmm-test.qianfan123.com:8311/dmm-web/'
    assert get_config(['dbo', 'base_url']) == 'yyy'
