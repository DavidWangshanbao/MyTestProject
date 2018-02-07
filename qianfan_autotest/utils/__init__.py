# coding=utf-8
from __future__ import unicode_literals, print_function
import os
import sys
import json

import requests
import six
import yaml
import codecs

##### 3d-party libs ######
from yaml import Loader, SafeLoader
from testcase import *

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'content-type': 'application/json;charset=utf-8'
}


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


def load_json_file(file_path, encoding='utf-8', **kwargs):
    """
    读取json格式文件
    :param file_path: json file path
    :return: python dict
    """
    with codecs.open(file_path, encoding=encoding) as fp:
        return json.load(fp, **kwargs)


def save_json_file(file_path, json_data, **kwargs):
    """
     保存成JSON格式的数据文件
    :param file_path: json输出文件路径
    :param json_data: 要被输出的数据
    :param kwargs: 其他参数
    :return:
    """
    with codecs.open(file_path, "w", encoding='utf-8') as  fp:
        json.dump(json_data, fp, **kwargs)


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


def baseurl_strip(baseurl):
    if baseurl.endswith('/'):
        baseurl = baseurl[:-1]
    return baseurl


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


class APICallHelper(object):
    """
    HTTP API请求的封装
    """
    # http method: GET,POST,PUT,DELETE,HEAD,OPTIONS
    _method = "GET"
    _headers = {}
    _params = {}
    _url = None
    _data = {}
    _auth = ()

    def __init__(self, session=None):
        self._session = session

    @property
    def session(self):
        return self._session

    def method(self, value):
        self._method = value.upper()
        return self

    def headers(self, json_str):
        if not isinstance(json_str, dict):
            d = json.loads(json_str, encoding='utf-8')
        else:
            d = json_str
        self._headers.update(d)
        return self

    def params(self, **kwargs):
        self._params.update(**kwargs)
        return self

    def body(self, json_str):
        if isinstance(json_str, six.string_types):
            # self._data = json.loads(json_str, encoding='utf-8')
            self._data = eval(json_str)
        else:
            self._data = json_str
        return self

    def request(self, url):
        self._url = url
        return self

    def auth(self, user, password):
        self._auth = (user, password)
        return self

    def perform(self, **kwargs):
        """

        :param kwargs:
        :return: Response对象
        """
        requests_kwargs = {"timeout": 5}

        if self._auth:
            requests_kwargs['auth'] = self._auth

        if self._headers:
            requests_kwargs['headers'] = self._headers

        if self._params:
            requests_kwargs['params'] = self._params

        if self._data:
            requests_kwargs['data'] = json.dumps(self._data, ensure_ascii=False).encode('utf-8')

        requests_kwargs = merge_dicts(requests_kwargs, kwargs)

        if self._session:
            response = self._session.request(method=self._method, url=self._url, **requests_kwargs)
        else:
            response = requests.request(method=self._method, url=self._url, **requests_kwargs)

        # if response.status_code != 200:
        #     raise ValueError("return code of http request is not 200")

        return response


def curl(url, session=None):
    api_caller = APICallHelper(session)
    import urlparse
    res = urlparse.urlsplit(url)

    api_caller._url = url.replace('?{}'.format(res.query), '')
    if res.query:
        _params = res.query.split('&')
        for x in _params:
            _s = x.split('=')
            api_caller.params(**{_s[0]: _s[1]})
    return api_caller
