# -*- coding: utf-8 -*-

import os, sys
import numpy as np


__all__ = ['stackgray2rgb',
           'graymask2rgb',
           ]


def stackgray2rgb(gray):
    """Stack three same gray image to 2 rgb image.
    """
    assert len(gray.shape) in [2, 3], "Gray image shape error"
    if len(gray.shape) == 3:
        assert gray.shape[2] == 1, "Not a proper gray image"
        gray = np.squeeze(gray, axis=2)

    if np.amax(gray) <= 1.0:
        gray = (gray * 255.0).astype(np.uint8)

    rgb_img = np.stack((gray, ), axis=-1)
    return rgb_img


def graymask2rgb(mask, channel=0):
    # Assert image shape
    assert len(mask.shape) in [2, 3], "Mask shape error"
    if len(mask.shape) == 3:
        assert mask.shape[2] == 1, "Not a proper mask"

    if np.amax(mask) <= 1.0:
        mask = (mask * 255.0).astype(np.uint8)
    zero_img = np.zeros((mask.shape[0], mask.shape[1]), np.uint8)

    # RGB image rely on channel value
    if channel == 'r' or channel == 'R' or channel == '0' or channel == 0:
        mask_rgb = np.stack((mask, zero_img, zero_img), axis=2)
    elif channel == 'g' or channel == 'G' or channel == '1' or channel == 1:
        mask_rgb = np.stack((zero_img, mask, zero_img), axis=2)
    elif channel == 'b' or channel == 'B' or channel == '2' or channel == 2:
        mask_rgb = np.stack((zero_img, zero_img, mask), axis=2)
    else:
        raise Exception("unknown parameter channel")

    return mask_rgb
