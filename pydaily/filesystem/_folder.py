# -*- coding: utf-8 -*-

import os
import shutil

__all__ = ['overwrite_dir',
           'check_mkdir',
           ]

def overwrite_dir(dir_name):
    """ Overwrite directory if exist, create new directory

    """

    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)



def check_mkdir(dir_name):
    """ if directory not exist, create the directory

    """

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
