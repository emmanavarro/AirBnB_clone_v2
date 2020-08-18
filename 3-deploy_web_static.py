#!/usr/bin/python3
""" deploy with fabric of static files of aribnb
"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['34.74.148.216', '52.91.39.101']


def do_pack():
    """ Pack a directory in a .tgz file  """
    local('mkdir -p versions')
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_time = 'versions/web_static_{}.tgz'.format(time)
    compressed = local("tar -cvzf " + file_time + " web_static/")
    if compressed.succeeded:
        return file_time
    return None


def do_deploy(archive_path):
    """ Deploy the airbnb static """
    if not path.exists(archive_path):
        return False
    ret_value = True
    try:
        up_dir = put(archive_path, '/tmp/')
        archive_file = archive_path.split(".")[0].split("/")[1]
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_file))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(archive_file, archive_file))
        run('rm /tmp/{}.tgz'.format(archive_file))
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(archive_file, archive_file))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_file))
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{}/ \
            /data/web_static/current'.format(archive_file))
    except Excepction:
        return False
    return True


def deploy():
    """ Deploy all """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
