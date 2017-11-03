# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.filesystem import is_image_file
from pydaily import DATA_DIR


def test_is_image_file():
    test_file1 = os.path.join(DATA_DIR, 'input/stomach/crop_patch/p0029.tiff')
    img_flag = is_image_file(test_file1)
    if img_flag == True:
        print("{} is an image file".format(test_file1))
    else:
        print("{} is not an image file".format(test_file1))

    test_file2 = os.path.join(DATA_DIR, 'README.md')
    img_flag = is_image_file(test_file2)
    if img_flag == True:
        print("{} is an image file".format(test_file2))
    else:
        print("{} is not an image file".format(test_file2))



if __name__ == '__main__':
    test_is_image_file()
