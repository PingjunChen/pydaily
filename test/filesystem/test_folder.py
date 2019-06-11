# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from filesystem import overwrite_dir, check_mkdir


def test_overwrite_dir():
    out_dir= os.path.join(TEST_PATH, "data/output")
    overwrite_dir(out_dir)

def test_check_mkdir():
    out_dir= os.path.join(TEST_PATH, "data/output")
    check_mkdir(out_dir)
