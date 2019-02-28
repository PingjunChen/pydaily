# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from format import dict_to_json, json_to_dict


def test_json():
    test_dict = {"names": ["Dina", "Irina", "Kennedy"],
                 "ages": [23, 31, 19]}
    # save as csv file
    test_json_path = os.path.join(TEST_PATH, "data/test.json")
    dict_to_json(test_dict, test_json_path)

    # load from csv file
    cur_dict = json_to_dict(test_json_path)
