# -*- coding: utf-8 -*-

import os, sys
import shutil

__all__ = ['overwrite_dir',
           ]


def overwrite_dir(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
