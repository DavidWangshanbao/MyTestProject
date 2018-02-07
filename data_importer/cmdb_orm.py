from __future__ import unicode_literals
from peewee import *
from playhouse.shortcuts import *
#  automatically generate cmdb orm entites
# python -m pwiz -e mysql -H rm-bp131v5wi2i6vg262.mysql.rds.aliyuncs.com -p 3306 -u somkeplat -P somkeplatD123 cmdb

# database = MySQLDatabase('cmdb', **{'host': 'rm-bp131v5wi2i6vg262.mysql.rds.aliyuncs.com', 'password': 'somkeplatD123', 'port': 3306, 'user': 'somkeplat'})
from playhouse.pool import PooledMySQLDatabase

from const import RDS_TIMEOUT
from settings import get_config
dnet_global_confg = get_config()
import json, os

filename = dnet_global_confg['cmdb_cfg']
database = None
with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
    ds = json.load(fp)[u"datasource"]
    # ds['database'] = ds['db']
    # ds= keyfilter(lambda k: k not in ['db','charset'], ds)
    # from pprint import  pprint
    # pprint(ds)
    database = PooledMySQLDatabase(host=ds['host'], user=ds['user'], passwd=ds['password'], database=ds['db'],
                                   charset=ds['charset'],
                                   connect_timeout=RDS_TIMEOUT, read_timeout=RDS_TIMEOUT, write_timeout=RDS_TIMEOUT)

# ==============================================================
#  PLEASE DO NOT CHANGE THE ABOVE SETTINGS
# ==============================================================
from hdtoolsetcore.cmdb import peewee_database

peewee_database.initialize(database)
from hdtoolsetcore.cmdb.cmdb import *
from hdtoolsetcore.cmdb.cmdbservice import *