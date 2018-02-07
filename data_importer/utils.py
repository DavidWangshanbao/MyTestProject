#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function, unicode_literals
import sys

import six

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import zipfile
import random
import datetime
import subprocess
import sys
import uuid
import yaml
import codecs
import re
import requests
import json
import argparse
from contextlib import contextmanager
from yaml import Loader, SafeLoader
from itertools import starmap
from toolz import keyfilter, pluck, concat, concatv, accumulate, join, merge, curry


def glob(path, pattern="*", recursive=True, absolute=True):
    '''
    Example: glob('.','*.tpl'):
    :param path:  搜索路径
    :param pattern: 正则表达式匹配文件路径
    :return:
    '''
    if recursive:
        import os, fnmatch
        for root, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, pattern):
                if absolute:
                    yield os.path.abspath(os.path.join(root, filename))
                else:
                    yield os.path.join(root, filename)
    else:
        import os
        from glob import glob
        for filename in glob("{}/{}".format(path, pattern)):
            if absolute:
                yield os.path.abspath(os.path.join(os.path.curdir, filename))
            else:
                yield os.path.join(os.path.curdir, filename)


# Example:
#       @coroutine
#       def grep(pattern):
def coroutine(func):
    def wrapper(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr

    return wrapper


def combine(a, b):
    for x in a:
        for y in b:
            yield x, y


def unzip(seq):
    '''
    Inverse of zip

    >>> a, b = unzip([('a', 1), ('b', 2)])
    >>> list(a)
    ['a', 'b']
    >>> list(b)
    [1, 2]
    '''
    from toolz.sandbox.core import unzip
    return unzip(seq=seq)


def keyjoin(leftkey, leftseq, rightkey, rightseq):
    '''
    Inner join two sequences of dictionaries on specified keys, merging matches with right value precedence.

    Example:
>>> people = [{'id': 0, 'name': 'Anonymous Guy', 'location': 'Unknown'},
              {'id': 1, 'name': 'Karan', 'location': 'San Francisco'},
              {'id': 2, 'name': 'Matthew', 'location': 'Oakland'}]
>>> hobbies = [{'person_id': 1, 'hobby': 'Tennis'},
               {'person_id': 1, 'hobby': 'Acting'},
               {'person_id': 2, 'hobby': 'Biking'}]
>>> list(keyjoin('id', people, 'person_id', hobbies))
[{'hobby': 'Tennis',
  'id': 1,
  'location': 'San Francisco',
  'name': 'Karan',
  'person_id': 1},
 {'hobby': 'Acting',
  'id': 1,
  'location': 'San Francisco',
  'name': 'Karan',
  'person_id': 1},
 {'hobby': 'Biking',
  'id': 2,
  'location': 'Oakland',
  'name': 'Matthew',
  'person_id': 2}]
    '''
    return starmap(merge, join(leftkey, leftseq, rightkey, rightseq))


def compact(iter):
    '''
    Filter an iterable on “truthy” values.

  Example:
    >>> results = [0, 1, 2, None, 3, False]
    >>> list(compact(results))
    [1, 2, 3]
    '''
    from toolz import filter
    return filter(None, iter)


def pluck_list(ind, seqs, default='__no__default__'):
    '''convert to list object for toolz.pluck'''
    return list(pluck(ind, seqs, default))


def concat_list(seqs):
    return list(concat(seqs=seqs))


def concatv_list(*seqs):
    return list(concatv(*seqs))


def accumulate_list(binop, seq, initial='__no__default__'):
    return list(accumulate(binop, seq, initial))


def pick(whitelist, d):
    '''Return a subset of the provided dictionary with keys contained in the whitelist.
    Example:
        >>> alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        >>> pick(['a', 'b'], alphabet)
        {'a': 1, 'b': 2}
    '''
    return keyfilter(lambda k: k in whitelist, d)


def omit(blacklist, d):
    '''Return a subset of the provided dictionary with keys not contained in the blacklist.
    Example:
        >>> alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        >>> omit(['a', 'b'], alphabet)
            {'c': 3, 'd': 4}
    '''
    return keyfilter(lambda k: k not in blacklist, d)


def listtodict(a):
    '''["a",1,"b",2] ==> {"a":1,"b":2}'''
    from itertools import izip
    i = iter(list(a))
    return dict(izip(i, i))


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        # print arcname
        zf.write(tar, arcname)
    zf.close()


def unzip_file(zipfilename, unziptodir):
    import re
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        # name = name.replace('\\', '/')
        name = re.sub('\\\\', '/', name)

        if name.endswith('/'):
            if not os.path.exists(os.path.join(unziptodir, name)):
                os.makedirs(os.path.join(unziptodir, name))
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            ext_dir = re.sub('\\\\', '/', ext_dir)
            if not os.path.exists(ext_dir): os.makedirs(ext_dir, 0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def normailize_path(path):
    """Normalize case of pathname.

        Makes all characters lowercase and all backslashes into slashes."""
    temp = re.sub('\\\\', '/', path)
    return temp


def __UUID__():
    return str(uuid.uuid4()).replace("-", '')


def __LINE__():
    try:
        raise Exception
    except Exception:
        return sys.exc_info()[2].tb_frame.f_back.f_lineno


def to_unicode(my_str):
    if (isinstance(my_str, str)):
        value = unicode(my_str, "utf-8")
    elif (isinstance(my_str, int) or isinstance(my_str, float)):
        value = unicode(my_str)
    else:
        value = my_str
    return value


def to_unicodegbk(my_str):
    if (isinstance(my_str, str)):
        value = unicode(my_str, "gbk")
    else:
        value = my_str
    return value


def getRandomHostId(stack_type):
    if (stack_type == u"plat"):
        id = random.randrange(start=0, stop=10000)
    else:
        id = random.randrange(start=10001, stop=9999999)
    return id


def autoGenerateStackId():
    CHAR_SET = [str(i) for i in range(10)]
    import string
    CHAR_SET.extend(string.lowercase)  # 'a' .. 'z'
    result = ""
    for i in range(4):
        result += CHAR_SET[random.randrange(start=0, stop=35)]
    return result


def save_yaml(filename, data, **kwargs):
    with codecs.open(filename, 'w', 'utf-8') as fp:
        # kwargs = merge_dicts(kwargs, {
        #     "default_flow_style": False,
        #     "explicit_start": True
        # })
        yaml.safe_dump(data, fp, allow_unicode=True, **kwargs)


def load_yaml(filename="settings.yaml"):
    # https://stackoverflow.com/questions/5484016/how-can-i-do-string-concatenation-or-string-replacement-in-yaml
    ''' load yaml file
        make sure it is unicode format

        include yaml files within yaml files
        link: http://virantha.com/2013/09/04/pyyaml-include-yaml-files-within-yaml-files/
        An example:
            foo.yaml

            a: 1
            b:
                - 1.43
                - 543.55
            c: !include bar.yaml
            bar.yaml

            - 3.6
            - [1, 2, 3]
            Now the files can be loaded using:

            >>> with open('foo.yaml', 'r') as f:
            >>>    data = yaml.load(f, Loader)
            >>> data
            {'a': 1, 'b': [1.43, 543.55], 'c': [3.6, [1, 2, 3]]}
    '''
    if (not filename):
        raise ValueError("filename in method `load_yaml` is None")

    def construct_yaml_str(self, node):
        # Override the default string handling function
        # to always return unicode objects
        return self.construct_scalar(node)

    def yaml_include(loader, node):
        # Get the path out of the yaml file
        file_name = os.path.join(os.path.dirname(loader.name), node.value)

        with file(file_name) as inputfile:
            return yaml.load(inputfile)

    def join(loader, node):
        ## using your sample data
        # yaml.load("""
        #   user_dir: &DIR /home/user
        #   user_pics: !join [*DIR, /pics]
        # """)
        # Which
        # results in:
        #
        # {'user_dir': '/home/user', 'user_pics': '/home/user/pics'}
        seq = loader.construct_sequence(node)
        return ''.join([str(i) for i in seq])

    Loader.add_constructor("!include", yaml_include)
    Loader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)
    Loader.add_constructor('!join', join)
    SafeLoader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)

    with open(filename, "r") as fp:
        res = yaml.load(fp.read())
    return res


def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        if dictionary is not None:
            result.update(dictionary)
    return result


def installPythonLibs(libs=[], mandatory=False):
    if (mandatory == True and len(libs) > 0):
        writeLinesToFile("requires.txt", libs)
        p = subprocess.Popen("pip install --upgrade -r requires.txt")
        return_code = p.wait()
        if (return_code != 0):
            raise Exception("find error when run pip install")


def readFromFile(filename, encoding=None):
    result = None
    encoding = encoding or 'utf-8'
    with codecs.open(filename, encoding=encoding) as fp:
        result = fp.read()
    return result


def readLinesFromFile(filename, encoding=None):
    encoding = encoding or 'utf-8'
    with codecs.open(filename, encoding=encoding) as fp:
        for line in fp.readlines():
            yield line


def writeLinesToFile(filename, lines, append=False, encoding=None):
    if (append == True):
        file_mode = "a"
    else:
        file_mode = "w"
    encoding = encoding or 'utf-8'
    with codecs.open(filename, file_mode, encoding=encoding) as fp:
        for line in lines:
            print(to_unicode(line), file=fp)
            # print(unicode(line, encoding), file=fp)


# 处理properties 文件末尾没有换行，导致mapping时候异常，而不影响其他的
def writeLinesToProperties(filename, lines, append=False):
    if (append == True):
        file_mode = "a"
    else:
        file_mode = "w"
    encoding = "utf-8"
    with codecs.open(filename, file_mode, encoding=encoding) as fp:
        print("\r", file=fp)
        for line in lines:
            print(to_unicode(line), file=fp)


def enum(*args):
    enums = dict(zip(args, range((len(args)))))
    return type(str("Enum"), (), enums)


# if __name__ == "__main__":
#     dict1 = {"a": 1, "b": 2}
#     dict2 = {"b": 3, "c": 4}
#     result = merge_dicts(dict1, dict2)
#     assert result["a"] == 1
#     assert result["b"] == 3
#     assert result["c"] == 4




def printStack(file=None):
    import traceback, sys

    traceback.print_exc(file=sys.stdout if file is None else file)


def download_file(url, output_file):
    """ download a file from given url"""
    from urllib2 import urlopen  # Python 2
    # from urllib.request import urlopen # Python 3

    response = urlopen(url)
    CHUNK = 16 * 1024
    with open(output_file, 'wb') as f:
        while True:
            chunk = response.read(CHUNK)
            if not chunk: break
            f.write(chunk)


# string convert timestamp
def formatTimetoTimestamp(datetimeStr, formats):
    import time
    timeArray = time.strptime(datetimeStr, formats)
    timeStamp = time.mktime(timeArray)  # to timestamp
    return timeStamp


@curry
def getbeforenow(day=1):
    oneday = datetime.timedelta(days=day)
    return datetime.datetime.now() - oneday


def getContainerName(containerId):
    """
    约定通过对containerId 用 '__' 分割取出第一个为contianer name
    :param containerId:
    :return contaiername:
    """
    return containerId.split("__")[0]


def get_jenkins_changeset(url):
    _url = "{0}/api/json?tree=changeSet[*[*]]".format(url)
    import json
    res = requests.get(_url, timeout=8, auth=("buhaiqing", "buhaiqing"))
    result = json.dumps(res.text, ensure_ascii=False)
    return result


def flatten_dict(config_data):
    """
    odict = {
    "a" :{
        "b": {
            "c":1,
            "d": 2
        }
    }
}
print(dict(flatten_dict(odict)).get('a.b.c')) # return 1
print(dict(flatten_dict(odict)).get('a.b.d')) # return 2
    """

    def __flat_dict(config_data):
        for key, value in six.iteritems(config_data):
            if hasattr(value, 'items') or hasattr(value, 'iteritems'):
                for k, v in __flat_dict(value):
                    yield '%s.%s' % (key, k), v
                continue

            yield key, value

    return dict(__flat_dict(config_data))


def csv_reader(file_obj):
    """
    Read a csv file
    """
    import csv
    reader = csv.reader(file_obj)
    for row in reader:
        yield row


def csv_writer(data, path):
    """
    Write data to a CSV file path
     data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    path = "output.csv"
    csv_writer(data, path)
    """
    import csv
    from module_utils._text import to_bytes
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=to_bytes(','))
        for line in data:
            writer.writerow(line)


def jsonify(result, format=False, sort_key=True):
    ''' format JSON output (uncompressed or uncompressed) '''

    if result is None:
        return "{}"

    indent = None
    if format:
        indent = 4

    try:
        return json.dumps(result, sort_keys=sort_key, indent=indent, ensure_ascii=False)
    except UnicodeDecodeError:
        return json.dumps(result, sort_keys=sort_key, indent=indent)


def is_port_open(ip, port):
    """用以判断机器上的端口是否被占用"""
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        # print ('%d is open' % port)
        return True
    except:
        # print ('%d is down' % port)
        return False


def _unique(fn):
    """
    @_unique
    def test():
        return [1,2,2,3,]

    print(list(test())) # [1, 2, 3]
    """
    import functools
    @functools.wraps(fn)
    def unique(*args, **kw):
        seen = set()
        for item in fn(*args, **kw):
            if item not in seen:
                seen.add(item)
                yield item

    return unique


class ArgumentParserError(Exception):
    pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


def fmt_val(val, shorten=True):
    """Format a value for inclusion in an
    informative text string.
    """
    from module_utils._text import to_text
    val = to_text(val)
    max = 50
    if shorten:
        if len(val) > max:
            close = val[-1]
            val = val[0:max - 4] + "..."
            if close in (">", "'", '"', ']', '}', ')'):
                val = val + close
    return val


def fmt_dict_vals(dict_vals, shorten=True):
    """Returns list of key=val pairs formatted
    for inclusion in an informative text string.
    """
    items = dict_vals.items()
    if not items:
        return [fmt_val(None, shorten=shorten)]
    return ["%s=%s" % (k, fmt_val(v, shorten=shorten)) for k, v in items]


def deep_update_dict(origin_dict, override_dict):
    """ update origin dict with override dict recursively
    e.g. origin_dict = {'a': 1, 'b': {'c': 2, 'd': 4}}
         override_dict = {'b': {'c': 3}}
    return: {'a': 1, 'b': {'c': 3, 'd': 4}}
    """
    for key, val in override_dict.items():
        if isinstance(val, dict):
            tmp = deep_update_dict(origin_dict.get(key, {}), val)
            origin_dict[key] = tmp
        else:
            origin_dict[key] = override_dict[key]

    return origin_dict


def get_excel_data(_dir):
    """
    读取根目录，返回表格数据
    :param _dir:
    :return:
    """
    ret = []

    def __read_excel(_dir):
        """
        读取excel文件列表
        :param _dir: 根目录
        :return:
        """
        for filename in glob(_dir, "*.xlsx"):
            yield filename

    # from tablib import Dataset
    from pandas.io.api import read_excel
    for filename in __read_excel(_dir):
        data = read_excel(filename)
        # data = Dataset().load(open(filename).read(), 'xlsx')
        ret.extend(data.to_dict('record'))
    return ret


DEFAULT_COLUMNS = ['created', 'domain', 'serverurl', 'requestid', 'size']


def export_shopids(filename='shopid.xlsx', sql_query='select id as shopid from cmdbshop where stackId in ("a03a","a02a","a01a") GROUP BY stackId,dbname'):
    from cmdb_orm import database
    import pandas.io.sql as sql
    df = sql.read_sql_query(
        sql_query,
        database.get_conn())

    df.to_excel(filename, index=False)
