# -*- coding: utf-8 -*-

import os

__all__ = ['find_ext_files',
           ]


def find_ext_files(dir_name, ext):
    """ Find all files with given extension in a given directory

    Parameters
    -------
    dir_name: str
        given directory to locate files
    ext: str
        file extension

    Returns
    -------
    file_list: list
        files with specified extesion in given directory

    """
    if not os.path.isdir(dir_name):
        raise AssertionError("{} is not a valid directory".format(dir_name))

    file_list = []
    for root, _, files in os.walk(dir_name):
        for cur_file in files:
            if cur_file.endswith(ext):
                 file_list.append(os.path.join(root, cur_file))

    return file_list
