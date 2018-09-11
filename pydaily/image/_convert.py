# -*- coding: utf-8 -*-

import os, sys
import numpy as np

__all__ = ['PIL2NpArr',
           ]

def PIL2NpArr(img):
    np_img = np.asarray(img)
    if np_img.shape[2] == 4:
        np_img = np_img[...,:-1]
    return np_img
