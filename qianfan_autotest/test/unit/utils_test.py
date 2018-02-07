#coding=utf-8
from pprint import pprint

import pytest
import unittest

import six

from utils import flatten_dict, APICallHelper


@pytest.mark.unit
class APICallHelperTest(unittest.TestCase):
    def setUp(self):
        self.api = APICallHelper()

    def test1(self):
        for method in ['post', 'get', 'put', 'delete', 'head']:
            self.api.method(method)
            self.assertEqual(self.api._method, method.upper())

    def test2(self):
        header_str = '''
                    {
                        "Accept": "application/json;charset=UTF-8"
                    }
                    '''
        body_str = '''
        {
           "key1": 1,
           "key2": 2
        }
        '''
        self.api.method('post').headers(header_str).body(body_str).params(key1='value1', key2='value2')
        self.assertIsNotNone(self.api._headers.get('Accept', None))
        pprint(self.api._headers)
        self.assertIsNotNone(self.api._data.get('key1', None))
        pprint(self.api._data)
        self.assertDictEqual(self.api._params, {
            "key1": "value1",
            "key2": "value2"
        })

@pytest.mark.unit
class UtilsTest(unittest.TestCase):
    def test_flattern_dict(self):
        odict = {
            "a": {
                "b": {
                    "c": 1,
                    "d": 2
                }
            }
        }
        self.assertEqual(dict(flatten_dict(odict)).get('a.b.c'),1)
        self.assertEqual(dict(flatten_dict(odict)).get('a.b.d'),2)

    def test_config_yaml(self):
        from libs.config import load_config,get_cfg_object
        load_config()
        cfg_obj = get_cfg_object()
        assert  cfg_obj
        flattern_obj = flatten_dict(cfg_obj)
        for k,v in six.iteritems(flattern_obj):
            _l = k.split(',')
            for item in _l:
                self.assertNotIn('-',item)


if __name__ == '__main__':
    pytest.main([__file__,'-sv'])