# -*- coding: utf-8 -*-

import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
PKG_NAME = os.path.basename(BASE_PATH)

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(PKG_NAME, parent_package, top_path)

    config.add_subpackage('filesystem')
    config.add_subpackage('format')
    config.add_subpackage('log')
    config.add_subpackage('tic')

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup

    config = configuration(top_path='').todict()
    setup(**config)
