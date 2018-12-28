# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))
DATA_DIR = os.path.join(TEST_PATH, "data")

from filesystem import overwrite_dir

def test_overwrite_dir():
    out_dir = os.path.join(DATA_DIR, 'output')
    overwrite_dir(out_dir)
