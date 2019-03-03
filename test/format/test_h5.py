# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from format import dict_to_h5, h5_to_dict


def test_h5():
    test_dict = {"names": ["Dina", "Irina", "Kennedy"],
                 "ages": [23, 31, 19]}
    # save as csv file
    test_h5_path = os.path.join(TEST_PATH, "data/test.h5")
    dict_to_h5(test_dict, test_h5_path)

    # load from csv file
    cur_dict = h5_to_dict(test_h5_path)

    if test_dict != cur_dict:
        raise AssertionError("dict not equal")
