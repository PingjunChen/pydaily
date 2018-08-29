# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.image import graymask2rgb
from pydaily import DATA_DIR

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def test_graymask2rgb():
    mask_img_path = os.path.join(DATA_DIR, "input/thyroid/mask/1273169.png")
    assert os.path.exists(mask_img_path), "{} not a valid file".format(mask_img_path)

    try:
        mask_img = misc.imread(mask_img_path)
    except:
        print("Load {} error.".format(mask_img_path))

    plt.imshow(mask_img, cmap='gray')
    plt.show()

    mask_rgb = graymask2rgb(mask_img, channel='r')
    plt.imshow(mask_rgb)
    plt.show()

if __name__ == '__main__':
    test_graymask2rgb()
