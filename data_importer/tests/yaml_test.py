# coding=utf-8
import unittest

import mock
import pytest
from ddt import ddt, data

from settings import get_config, get_email_subject_setting, get_ssh_port, getSettings
from utils import load_yaml

dnet_global_confg = get_config()

'''测试settings.yaml,docker_environment.yaml的格式是否正确，是yaml格式'''


@ddt
@pytest.mark.unit
@pytest.mark.yaml
class YamlsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_settings(self):
        try:
            result = dnet_global_confg
            self.assertIsNotNone(result)
        except Exception as err:
            print err

    @mock.patch("settings.get_env_product")
    @mock.patch("settings.get_env_base_profile")
    @mock.patch("settings.get_env_active_profile")
    @mock.patch("settings.get_preset_image_version")
    @data(('dnet', 'branch_test'),
          ('dnet', 'production'),
          ('scm', 'branch_test'),
          ('scm', 'production'),
          ('dly', 'branch_test'),
          ('dly', 'production'),
          ('pluto', 'branch_test'),
          ('pluto', 'production'))
    def test_get_settings(self, item, mock, mock_get_env_active_profile, mock_get_env_base_profile,
                          mock_get_env_product):
        (product, env) = item
        mock_get_env_active_profile.return_value = env
        mock_get_env_base_profile.return_value = "branch_test"
        mock_get_env_product.return_value = product
        mock.return_value = None
        try:
            from settings import getSettings
            getSettings(True)
        except Exception:
            self.fail("")


if __name__ == "__main__":
    errno = pytest.main([__file__, '-sv'])
    exit(errno)
