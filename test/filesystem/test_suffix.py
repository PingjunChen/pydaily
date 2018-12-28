# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))
DATA_DIR = os.path.join(TEST_PATH, "data")

from pydaily.filesystem import is_image_file


def test_is_image_file():
    test_file1 = os.path.join(DATA_DIR, 'input/AliceLake.jpg')
    img_flag = is_image_file(test_file1)
    if img_flag == True:
        print("{} is an image file".format(test_file1))
    else:
        print("{} is not an image file".format(test_file1))
