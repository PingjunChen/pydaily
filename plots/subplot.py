# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


def plot_lr(l_img, r_img, l_title=None, r_title=None, suptitle=None):

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

    axes[0].imshow(l_img)
    axes[0].set_title(l_title)

    axes[1].imshow(r_img)
    axes[1].set_title(r_title)

    plt.suptitle(suptitle, fontsize=16)
    plt.show()

if __name__ == '__main__':
    img1 = misc.imread('/home/pingjun/Desktop/SegPreds/n0253.png')
    img2 = misc.imread('/home/pingjun/Desktop/SegPreds/n0265.png')
    plot_lr(img1, img2, l_title="Left", r_title="Right", suptitle="Two Images")
