# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.images import blend_images
from pydaily.images import graymask2rgb
from pydaily import DATA_DIR

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


def test_blend_images():
    mask_path = os.path.join(DATA_DIR, "input/thyroid/mask/1273169.png")
    assert os.path.exists(mask_path), "{} not a valid file".format(mask_path)
    img_path = os.path.join(DATA_DIR, "input/thyroid/thumb_slide/1273169.png")
    assert os.path.exists(img_path), "{} not a valid file".format(img_path)
    # Read mask and image
    mask = misc.imread(mask_path)
    img = misc.imread(img_path)
    # Convert mask to rgb
    mask_rgb = graymask2rgb(mask, 'r')
    # combine img and mask_rgb
    combine = blend_images(img, mask_rgb, 0.8)

    plt.imshow(combine)
    plt.show()

if __name__ == '__main__':
    test_blend_images()
