# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from format import list_to_txt, txt_to_list


def test_txt():
    test_list = ["United States", "Japan", "China", "Israel"]

    # save as csv file
    test_txt_path = os.path.join(TEST_PATH, "data", "test.txt")
    list_to_txt(test_list, test_txt_path)

    # load from csv file
    cur_list = txt_to_list(test_txt_path)

    if test_list != cur_list:
        raise AssertionError("list not equal")
