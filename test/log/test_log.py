# -*- coding: utf-8 -*-

import os, sys

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from log import Logger

def test_log():
    logger = Logger()
    test_log_path = os.path.join(TEST_PATH, "data", "log.txt")
    logger.open(test_log_path)
    logger.write("Hello Logger")
