# -*- coding: utf-8 -*-

import os, sys

__all__ = ['is_image_file',
           ]


def is_image_file(filename):
    IMG_EXTENSIONS = [
        '.jpg', '.JPG', '.jpeg', '.JPEG',
        '.png', '.PNG',
        '.ppm', '.PPM',
        '.bmp', '.BMP',
        'tif', 'TIF', 'tiff', 'TIFF',
    ]

    img_flag = any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

    return img_flag
