# -*- coding: utf-8 -*-

import os, sys
import numpy as np


__all__ = ['overlay_bbox',
           ]

def overlay_bbox(im, boxes, rgb, stroke=1):
    """Method to overlay bounding boxes on image

    Parameters
    ----------
    boxes: list of box with [x_min, y_min, x_max, y_max]

    """
    row_size, col_size = im.shape[0:2]
    for box in boxes:
        # --- Extract coordinates
        box = [int(b) for b in box]
        x_min, y_min, x_max, y_max = box
        # Calculate bounding box bouondary
        l_shift = - ((stroke-1) // 2)
        r_shift = l_shift + stroke
        # draw bbox
        upper_start, upper_end = max(0, y_min + l_shift), min(row_size, y_min + r_shift)
        im[upper_start:upper_end, x_min:x_max, :] = rgb
        lower_start, lower_end = max(0, y_max + l_shift), min(row_size, y_max + r_shift)
        im[lower_start:lower_end, x_min:x_max, :] = rgb
        left_start, left_end = max(0, x_min + l_shift), min(col_size, x_min + r_shift)
        im[y_min:y_max, left_start:left_end, :] = rgb
        right_start, right_end = max(0, x_max + l_shift), min(col_size, x_max + r_shift)
        im[y_min:y_max, right_start:right_end, :] = rgb

    return im
