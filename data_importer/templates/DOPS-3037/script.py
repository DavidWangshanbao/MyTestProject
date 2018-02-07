dbname = "dmm"

def generate_sql(row, tempalte_file ,prefix ):
    """need to be overriden"""
    from cmdb import Cmdb
    from utils import merge_dicts, readFromFile, writeLinesToFile
    cmdb = Cmdb()
    dbinfo = cmdb.get_rds_info_by_dbname(dbname)
    result = readFromFile(tempalte_file)
    sql_file = "{}.sql".format(dbname)
    writeLinesToFile(sql_file, [result])
    return sql_file, dbinfo


def generate_cmd(row, template_file, __dir):
    """need to be overriden"""
    print('script:define sqlxx')