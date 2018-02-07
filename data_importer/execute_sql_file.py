# coding=utf-8
"""
以任务单号为目录名, 目录里存放：
－　*.xlsx Excel文件
-   xxx.j2 模板文件
-   script 生成执行脚本
"""
from __future__ import unicode_literals, print_function

import argparse
import os
from cmdb import get_rds_info_by_shopid
from utils import glob, merge_dicts, writeLinesToFile, readFromFile,  get_excel_data

exit_code = 0

def combine(a,b):
    for x in a:
        for y in b:
            yield x,y


def generate_sql(row, template_file, __dir):
    """need to be overriden"""
    id = row.get('shopid')
    dbinfo = get_rds_info_by_shopid(id)
    result = readFromFile(template_file)

    out = result.replace("{{ dbname }}", dbinfo.get("dbname"))
    sql_file = "{}.sql".format(id)
    writeLinesToFile(sql_file, [out])
    return sql_file, merge_dicts(row, dbinfo)


def generate_cmd(row, sql_file ):
    dd = merge_dicts(row, {"sql_file": sql_file})
    # if prefix :
    #     dd["dbname"] = "{prefix}_{dbname}".format(prefix = prefix ,dbname = dd["dbname"])
    cmd = "mysql -f -h{host} -u{username} -p{password} -P{port}  -D{dbname} --default-character-set=utf8  < ./{sql_file}".format(
        **dd)
    return cmd


def main(tempalte_files, data_set, __dir, dryrun ,prefix):
    import importlib
    m = importlib.import_module('templates.{}.script'.format(__dir))

    for row, tempalte_file in combine(data_set, tempalte_files):
        sql_file,data = m.generate_sql(row, tempalte_file ,prefix  )
        cmd = generate_cmd(merge_dicts(row,data) , sql_file )
        if dryrun:
            print(cmd)
        else:
            print(cmd)
            os.system(cmd)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', dest='dir', required=True, help="输入文件路径,建议以任务单号命名")
        parser.add_argument("-prefix" ,dest='prefix' ,required = False ,help = "新导入的数据库前缀")
        parser.add_argument('-dryrun', dest='dryrun', action="store_true")
        args = parser.parse_args()
        dryrun = args.dryrun
        prefix = args.prefix if args.prefix and args.prefix != "None" else None
        __dir = os.path.join('.', 'templates', args.dir)
        if not os.path.exists(__dir):
            raise ValueError("`{}` does not exists".format(__dir))

        # 1.获得sql 模板列表
        tempalte_files = list(glob(__dir, '*.j2'))
        # 2.从Excel获取需要修改的数据集
        data_set = get_excel_data(__dir)

        # 3. 生成sql file和执行它
        main(tempalte_files, data_set, args.dir, dryrun ,prefix)
    except Exception as e:
        print(e)
        exit_code = 1
    finally:
        exit(exit_code)
