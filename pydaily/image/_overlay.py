# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import cv2

from ._color import stackgray2rgb


__all__ = ['overlay_contour',
    'overlay_bbox',
    'overlay_box_label',
    ]


def overlay_bbox(im, boxes, rgb, stroke=1):
    """Method to overlay bounding boxes on image.

    Parameters
    ----------
    boxes: list of box with [x_min, y_min, x_max, y_max]

    """
    row_size, col_size = im.shape[0:2]
    l_shift = - ((stroke-1) // 2)
    r_shift = l_shift + stroke

    for box in boxes:
        # --- Extract coordinates
        box = [int(b) for b in box]
        x_min, y_min, x_max, y_max = box
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


def overlay_box_label(img, boxes, labels):
    """Method to overlay paired boxes and lables on image

    Parameters
    ----------
    boxes: list of box with [x_min, y_min, x_max, y_max]
    labels: label corresponded with box

    """

    font = cv2.FONT_HERSHEY_SIMPLEX
    for box, label in zip(boxes, labels):
        tl_pos, br_pos = (box[0], box[1]), (box[2], box[3])
        overlay = cv2.rectangle(img, tl_pos, br_pos, (255,0,0), 2)
        cv2.putText(overlay, label, tl_pos, font, 1, (255,255,255), 2, cv2.LINE_AA)

    return overlay


def overlay_contour(img, np_arr, rgb=(255, 0, 0), cnt_width=1):
    """Overlay contour on image.

    Parameters
    ----------
    img: numpy array
    np_arr: numpy 2d array [0]-w, [1]-h
    rgb: drawed contour color
    """

    arr_t = np_arr.transpose()
    cv_cnt = np.expand_dims(arr_t, axis=1)

    if len(img.shape) == 2 or (len(img.shape) == 3 and img.shape[2] == 1):
        img = stackgray2rgb(img)

    cnt_img = cv2.drawContours(img.copy(), [cv_cnt, ], 0, rgb, cnt_width)

    return cnt_img
