# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

FILE_PATH = os.path.abspath(__file__)
TEST_PATH = os.path.dirname(os.path.dirname(FILE_PATH))
PRJ_PATH = os.path.dirname(TEST_PATH)
sys.path.insert(0, os.path.join(PRJ_PATH, "pydaily"))

DATA_DIR = os.path.join(TEST_PATH, "data")
from image import graymask2rgb


# def test_graymask2rgb():
#     mask_img_path = os.path.join(DATA_DIR, "gray/gray123.png")
#     assert os.path.exists(mask_img_path), "{} not a valid file".format(mask_img_path)
#
#     try:
#         mask_img = misc.imread(mask_img_path)
#     except:
#         print("Load {} error.".format(mask_img_path))
#
#     plt.imshow(mask_img, cmap='gray')
#     plt.show()
#
#     mask_rgb = graymask2rgb(mask_img, channel='r')
#     # plt.imshow(mask_rgb)
#     # plt.show()
