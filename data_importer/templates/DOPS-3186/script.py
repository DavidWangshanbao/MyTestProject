
def generate_sql(row, template_file ,prefix):
    from cmdb import get_rds_info_by_shopid
    from utils import merge_dicts, readFromFile, writeLinesToFile

    id = row.get('shopid')
    dbinfo = get_rds_info_by_shopid(id)
    row = merge_dicts(row, dbinfo)
    result = readFromFile(template_file)

    out = result.replace("{{ dbname }}", row.get("dbname"))
    sql_file = "{}.sql".format(id)
    writeLinesToFile(sql_file, [out])
    return sql_file,row


def generate_cmd(row, template_file, __dir):
    """need to be overriden"""
    print('script:define sqlxx')