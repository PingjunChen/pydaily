# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))
DATA_DIR = os.path.join(TEST_PATH, "data")

from filesystem import find_ext_files

def test_find_ext_files():
    input_dir = os.path.join(DATA_DIR, 'input')
    ext = '.png'

    filelist = find_ext_files(input_dir, ext)

    if len(filelist) == 0:
        print("No file with given extension")
    else:
        print("There are {} files end with {}".format(len(filelist), ext))
        for ind, cur_file in enumerate(filelist):
            print("{}: {}".format(ind+1, cur_file))
