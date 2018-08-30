# -*- coding: utf-8 -*-

import os, sys
import numpy as np

__all__ = ['cal_confusion_matrix', 'cal_histogram',
            'cal_kappa', 'cal_linear_weighted_kappa',
            'cal_quadratic_weighted_kappa',
           ]

def cal_confusion_matrix(ra, rb, min_r=None, max_r=None):
    """Calculate the confusion matrix between two raters.
    """
    if type(ra) == np.ndarray:
        ra = ra.tolist()
    if type(rb) == np.ndarray:
        rb = rb.tolist()
    assert len(ra) == len(rb), "Two ratings are of different length"
    min_r = min(ra + rb) if min_r==None else min_r
    max_r = max(ra + rb) if max_r==None else max_r
    r_num = max_r - min_r + 1
    # Initial confusion matrix
    conf_mat = np.zeros((r_num, r_num), dtype=np.int32)
    for a, b in zip(ra, rb):
        conf_mat[a-min_r][b-min_r] += 1

    return conf_mat


def cal_histogram(ra, min_r=None, max_r=None):
    """Calculate rating's histogram.
    """
    min_r = min(ra) if min_r==None else min_r
    max_r = max(ra) if max_r==None else max_r
    r_num = max_r - min_r + 1
    hist = np.zeros((r_num,), dtype=np.int32)
    for r in ra:
        hist[r-min_r] += 1

    return hist


def cal_kappa(ra, rb, min_r=None, max_r=None):
    """Calculate Cohen's kappa for inter-rater agreement measuring
    """
    if type(ra) == np.ndarray:
        ra = ra.tolist()
    if type(rb) == np.ndarray:
        rb = rb.tolist()
    assert len(ra) == len(rb), "Two ratings are of different length"
    min_r = min(ra + rb) if min_r==None else min_r
    max_r = max(ra + rb) if max_r==None else max_r

    r_num = max_r - min_r + 1
    item_num = len(ra)
    conf_mat = cal_confusion_matrix(ra, rb, min_r, max_r)
    hist_a = cal_histogram(ra)
    hist_b = cal_histogram(rb)

    numerator, denominator = 0, 0
    for i in range(r_num):
        for j in range(r_num):
            expected_counts = (hist_a[i] * hist_b[j] * 1.0 / item_num)
            weight = 0.0 if i==j else 1.0
            numerator += weight * conf_mat[i][j] / item_num
            denominator += weight * expected_counts / item_num

    kappa_val = 1.0 - numerator / denominator

    return kappa_val


def cal_linear_weighted_kappa(ra, rb, min_r=None, max_r=None):
    """Calculate linear weighted kappa for inter-rater agreement measuring
    """
    if type(ra) == np.ndarray:
        ra = ra.tolist()
    if type(rb) == np.ndarray:
        rb = rb.tolist()
    assert len(ra) == len(rb), "Two ratings are of different length"
    min_r = min(ra + rb) if min_r==None else min_r
    max_r = max(ra + rb) if max_r==None else max_r

    r_num = max_r - min_r + 1
    item_num = len(ra)
    conf_mat = cal_confusion_matrix(ra, rb, min_r, max_r)
    hist_a = cal_histogram(ra)
    hist_b = cal_histogram(rb)

    numerator, denominator = 0, 0
    for i in range(r_num):
        for j in range(r_num):
            expected_counts = (hist_a[i] * hist_b[j] * 1.0 / item_num)
            weight = abs(i - j) * 1.0 / (r_num - 1)
            numerator += weight * conf_mat[i][j] / item_num
            denominator += weight * expected_counts / item_num

    linear_kappa_val = 1.0 - numerator / denominator

    return linear_kappa_val


def cal_quadratic_weighted_kappa(ra, rb, min_r=None, max_r=None):
    """Calculate quadratic weighted kappa for inter-rater agreement measuring
    """
    if type(ra) == np.ndarray:
        ra = ra.tolist()
    if type(rb) == np.ndarray:
        rb = rb.tolist()
    assert len(ra) == len(rb), "Two ratings are of different length"
    min_r = min(ra + rb) if min_r==None else min_r
    max_r = max(ra + rb) if max_r==None else max_r

    r_num = max_r - min_r + 1
    item_num = len(ra)
    conf_mat = cal_confusion_matrix(ra, rb, min_r, max_r)
    hist_a = cal_histogram(ra)
    hist_b = cal_histogram(rb)

    numerator, denominator = 0, 0
    for i in range(r_num):
        for j in range(r_num):
            expected_counts = (hist_a[i] * hist_b[j] * 1.0 / item_num)
            weight = pow(i - j, 2) * 1.0 / pow(r_num - 1, 2)
            numerator += weight * conf_mat[i][j] / item_num
            denominator += weight * expected_counts / item_num

    quadratic_kappa_val = 1.0 - numerator / denominator

    return quadratic_kappa_val
