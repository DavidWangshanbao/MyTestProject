# -*- coding: UTF-8 -*-
#  pip install requests
import commands
import requests
from const import HTTP_REQUEST_TIMEOUT


def checkDockerImage(url, username="dnet", password="ThlVjVebSKB5oTZ5"):
    r = requests.get(url, auth=(username, password), verify=False, timeout=HTTP_REQUEST_TIMEOUT)
    return r.status_code


def dockerLogin(url, username, password):
    command = "docker login -u {username} -p {password} {url}" \
        .replace('{username}', username) \
        .replace('{password}', password) \
        .replace('{url}', url)
    (status, output) = commands.getstatusoutput(command)
    return status, output


def pullImage(appName, appVersion, url, username, password):
    command = "docker login -u {username} -p {password} {url}; docker pull {url}/{appName}:{appVersion}" \
        .replace('{url}', url) \
        .replace('{appName}', appName) \
        .replace('{appVersion}', appVersion) \
        .replace('{username}', username) \
        .replace('{password}', password)
    (status, output) = commands.getstatusoutput(command)
    return status, output


def pushImage(appName, appVersion, url, username, password):
    command = "docker login -u {username} -p {password} {url}; docker push {url}/{appName}:{appVersion} " \
        .replace('{url}', url) \
        .replace('{appName}', appName) \
        .replace('{appVersion}', appVersion) \
        .replace('{username}', username) \
        .replace('{password}', password)
    (status, output) = commands.getstatusoutput(command)
    return status, output


def checkImage(docker_hub, imagelist, version, username, password):
    for i in xrange(len(imagelist)):
        # url = "https://{0}/uidnet/tag/{1}/{2}".format(docker_hub, imagelist[i], version)
        url = "https://{0}/tag/{1}/{2}".format(docker_hub, imagelist[i], version)
        has_error = False
        code = checkDockerImage(url, username, password)
        if code != 200:
            has_error = True
    return has_error


def ImageTag(sourceUrl, targetUrl, image, version):
    tagCommand = "docker tag {sourceUrl}/{image}:{version} {targetUrl}/{image}:{version}" \
        .format(sourceUrl=sourceUrl, targetUrl=targetUrl, image=image, version=version)
    (status, output) = commands.getstatusoutput(tagCommand)
    return status, output


def buildImage(dockerhub_url,image, tag,docker_file_folder='.'):
    (status, output) = commands.getstatusoutput("docker build -t {}/{}:{} {}".format(dockerhub_url,image, tag,docker_file_folder))
    return status,output
