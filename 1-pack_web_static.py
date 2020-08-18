#!/usr/bin/python3
""" Generate a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo """

from fabric.api import run, local
from datetime import datetime


def do_pack():
    """ Pack a directory in a .tgz file """

    local('mkdir -p versions')

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_time = 'versions/web_static_{}.tgz'.format(time)

    compressed = local("tar -cvzf " + file_time + " web_static/")

    if compressed.succeeded:
        return file_time
    return None
