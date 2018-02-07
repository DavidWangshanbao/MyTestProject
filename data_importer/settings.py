#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#  sample usage:
#     from settings import dnet_global_confg
#     print(dnet_global_confg)
from __future__ import unicode_literals
from toolz import pluck, compose, get_in
from utils import omit, pick
import os
from utils import load_yaml, merge_dicts
import staticconf

__config = None
__active_profile = None
__settings = None
DEFAULT_PRODUCT = 'dnet'


# dnet_global_confg = None
# active_profile
def get_base_dir():
    return os.path.dirname(os.path.realpath(__file__))


def get_env_active_profile():
    """当前profile"""
    return os.getenv("DNET_PROFILE", getSettings().get('active_profile'))
    # return os.getenv("DNET_PROFILE", staticconf.get('active_profile'))


def get_env_base_profile():
    """使用哪个profile为基准"""
    return os.getenv("DNET_BASE_PROFILE", getSettings().get('base_profile'))
    # return os.getenv("DNET_BASE_PROFILE", staticconf.get('base_profile'))


def get_env_product():
    """千帆的哪个产品DNET、分销、会员"""
    return os.getenv("DNET_PRODUCT", getSettings().get("product"))
    # return os.getenv("DNET_PRODUCT", staticconf.get('product').value)


def get_config(force_reload=False):
    CONFIG_NAMESPACE = 'DEFAULT'
    global __active_profile
    global __config
    global __settings
    if force_reload:
        __config = None
        __settings = None
    if __config == None:
        staticconf.reload(all_names=True)
        #  初始化setting.yaml
        __settings = load_yaml(os.path.join(get_base_dir(), "settings.yaml"))
        # staticconf.YamlConfiguration(os.path.join(get_base_dir(), "settings.yaml"), flatten=False,
        #                              namespace=CONFIG_NAMESPACE)
        __product = get_env_product()

        # 如果指定了具体产品的特殊配置，可以同时加载
        # for example: settings-scm.yaml, settings-dly.yaml
        _dict2= {}
        if __product != DEFAULT_PRODUCT:
            _fp = os.path.join(get_base_dir(), "settings-{}.yaml".format(__product))
            if os.path.exists(_fp):
                _dict2 = load_yaml(_fp)
            # staticconf.YamlConfiguration(os.path.join(get_base_dir(), "settings-{}.yaml".format(__product)),
            #                              flatten=False,
            #                              namespace=CONFIG_NAMESPACE, optional=True)

        __settings = merge_dicts(__settings,_dict2)
        staticconf.DictConfiguration(__settings, flatten=False, namespace=CONFIG_NAMESPACE)
        __active_profile = get_env_active_profile()
        print("active profile is {}".format(__active_profile))
        __base_profile = get_env_base_profile()
        # print("base profile is {}".format(__base_profile))
        print("product is {}".format(__product))

        # __config = merge_dicts(staticconf.get(__base_profile, namespace=CONFIG_NAMESPACE),
        #                        staticconf.get(__active_profile, namespace=CONFIG_NAMESPACE))
        __config = merge_dicts(__settings.get(__base_profile),__settings.get(__active_profile))




    return __config


def get_active_profile(force_reload=False):
    if force_reload == True or __active_profile == None:
        get_config(True)

    return __active_profile


def get_environment(force_reload=False):
    return get_config(force_reload)['stack_environment']

def get_images_dag_config(force_reload=False):
    _config = getSettings(force_reload)
    return _config.get('subsystems_dag')



def getSettings(force_reload=False):
    if force_reload or __settings==None:
        get_config(force_reload=True)
    return __settings


def get_appabout():
    s = get_config()['appAbout']
    return s


def getLogstashSetting():
    s = get_config()['logstash']
    return (s['url'], s['user'], s['password'])


def getElasticSearchSetting():
    s = get_config()['elasticsearch']
    return (s['host'], s['port'], s['user'], s['password'])



def get_dnet_subsystems():
    DNET_SUBSYSTEMS = filter(lambda x: x not in get_infra_subsystems(), get_config()['inventory'].keys())
    return DNET_SUBSYSTEMS

def get_infra_subsystems():
    return ['filebeat', 'logstash', 'elasticsearch', 'kibana']

def getDnetSubsystemConfig():
    return omit(get_infra_subsystems(), get_config()['inventory'])


def getInventoryImages(subsystem):
    result = pick([subsystem], get_config()['inventory'])
    return get_in(['images'], pick(['images'], result[subsystem]))


def get_preset_image_version():
    return os.environ.get("PRESET_IMAGE_VERSION")

def getInventoryDescription(imageName, force_reload=False):
    from toolz import keyfilter, get_in
    inventory = get_config(force_reload)['inventory']
    o = keyfilter(lambda x: imageName in inventory[x]["images"], inventory)
    return get_in([o.keys()[0], 'description'], o)




def getInventoryImageLabels(imageName, force_reload=False):
    from toolz import keyfilter, get_in
    inventory = get_config(force_reload)['inventory']
    o = keyfilter(lambda x: imageName in inventory[x]["images"], inventory)
    return get_in([o.keys()[0], 'labels'], o)


def get_deployment_label(sub_system, force_reload=False):
    return get_config(force_reload)['inventory'][sub_system]['labels']['deployment']


def imageMatrix():
    inventory = getDnetSubsystemConfig()
    image_data = []
    for sub_system in inventory.keys():
        data = inventory[sub_system]
        images = data['images']
        version = data['version']
        image_len = len(images)
        image_data.extend(zip([sub_system] * image_len, images, [version] * image_len))
    return image_data


def getToolsetserviceProfile():
    __toolsetservice = os.getenv("TOOLSETSERVICE_PROFILE")
    return __toolsetservice or "smoke_test"


def getELKConfig(force_reload=False):
    return get_config(force_reload=force_reload)['elasticsearch']


def getInventoryImageConditionRules(imageName):
    from toolz import keyfilter, get_in
    inventory = get_config()['inventory']
    o = keyfilter(lambda x: imageName in inventory[x]["images"], inventory)
    return get_in([o.keys()[0], 'conditions_rules'], o)


def get_rds_upgrade_config(sub_systems=None):
    rds_upgrade = dict()
    for sub_system, data in get_config()['inventory'].iteritems():
        if sub_systems and sub_system not in sub_systems:
            continue
        if data.has_key("rds_upgrade"):
            if isinstance(data['rds_upgrade'], list):
                for image in data['rds_upgrade']:
                    rds_upgrade[image['image']] = merge_dicts({"version": data['version']}, image)
            else:
                rds_upgrade[data['rds_upgrade']['image']] = merge_dicts({"version": data['version']},
                                                                        data['rds_upgrade'])
    from pprint import pprint
    pprint(rds_upgrade)
    return rds_upgrade


def get_docker_hub_config(force_reload=False):
    _config = getSettings(force_reload)
    return _config.get('dockerhub')


def get_docker_hub_info(cmdb=None):
    if cmdb is None:
        from cmdb import Cmdb
        cmdb = Cmdb()

    dockerhub = cmdb.getDockerHub()
    dockhub_url = dockerhub.url
    username = dockerhub.username
    password = dockerhub.password
    return dockhub_url, username, password


def get_email_subject_setting(force_reload=False):
    _config = getSettings(force_reload)
    return _config.get('email_settings')


def get_dnet_version(force_reload=False):
    _config = getSettings(force_reload)
    return _config.get('dnet_version')




def get_ssh_port(force_reload=False):
    _config = get_config(force_reload)
    return _config.get('ssh_port') or "60501"



if __name__ == "__main__":
    '''负责产生依据环境的配置清单，请在发布前进行复查
    Example:
      DNET_PROFILE=production python settings.py
    '''

    try:
        import json, codecs, sys

        outputfile = os.environ.get('OUTPUT_FILE', "active_profile.json")
        with codecs.open(outputfile, "w", encoding='utf-8') as  fp:
            get_config().items().sort()
            json.dump(get_config(), fp, indent=4)
    except Exception as e:
        print(unicode(e))
    else:
        print("{0} is generated succesfully".format(outputfile))
