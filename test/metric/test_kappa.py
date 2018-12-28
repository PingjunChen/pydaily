# -*- coding: utf-8 -*-

import os, sys
import numpy as np

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

from metric import cal_confusion_matrix
from metric import cal_histogram
from metric import cal_kappa
from metric import cal_linear_weighted_kappa
from metric import cal_quadratic_weighted_kappa


def test_cal_confusion_matrix():
    r1 = [1, 3, 4, 2, 5, 2, 3, 4, 2, 3]
    r2 = [1, 2, 4, 2, 4, 3, 3, 5, 2, 3]

    conf_mat = cal_confusion_matrix(r1, r2)
    print("Confusion matrix is:")
    print(conf_mat)

def test_cal_histogram():
    r1 = [1, 3, 4, 2, 5, 2, 3, 4, 2, 3]
    hist = cal_histogram(r1)
    print("Histogram is:")
    print(hist)

def test_cal_kappa():
    r1 = [1, 5, 4, 2, 5, 2, 3, 4, 2, 3]
    r2 = [1, 2, 4, 2, 5, 3, 3, 4, 2, 3]

    kappa_val = cal_kappa(r1, r2)
    linear_kappa_val = cal_linear_weighted_kappa(r1, r2)
    quadratic_kappa_val = cal_quadratic_weighted_kappa(r1, r2)
    print("Kappa value is: {}".format(kappa_val))
    print("Linear Kappa value is: {}".format(linear_kappa_val))
    print("Quadratic Kappa value is: {}".format(quadratic_kappa_val))
