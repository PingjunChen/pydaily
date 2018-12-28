# -*- coding: utf-8 -*-

import os, sys
import numpy as np

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from tic import time_to_str

def test_time_to_str():
    from timeit import default_timer as timer
    start = timer()
    elapsed_time_str = time_to_str(timer() - start, "sec")
    print("Elasped time is: {}".format(elapsed_time_str))
