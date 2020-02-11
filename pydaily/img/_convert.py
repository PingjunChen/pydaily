# -*- coding: utf-8 -*-

import numpy as np

__all__ = ['PIL2npArr',
           'Bool2Uint8',
           'Binary2Bool'
           ]


def PIL2npArr(pil_img):
    """ Convert Pillow image to numpy array.

    """

    np_img = np.asarray(pil_img)
    if len(np_img.shape) == 2:
        pass
    elif len(np_img.shape) == 3:
        if np_img.shape[2] == 4:
            np_img = np_img[...,:-1]
    else:
        raise NotImplementedError()

    return np_img


def Bool2Uint8(bool_img):
    """ Convert bool image to dtype uint8.

    """

    u_img = bool_img.astype(np.uint8)

    return u_img


def Binary2Bool(bin_img):
    """ Convert binary image to dtype bool.

    """

    max_val = np.amax(bin_img)
    bool_img = (bin_img / max_val).astype('bool')

    return bool_img
