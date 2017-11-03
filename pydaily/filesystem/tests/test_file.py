# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.filesystem import find_ext_files
from pydaily import DATA_DIR


def test_find_ext_files():
    input_dir = os.path.join(DATA_DIR, 'input')
    ext = '.png'

    filelist = find_ext_files(input_dir, ext)

    if len(filelist) == 0:
        print("No file with given extension")
    else:
        print("There are {} files end with {}".format(len(filelist), ext))
        for ind, cur_file in enumerate(filelist):
            print("{}: {}".format(ind+1, cur_file))

if __name__ == '__main__':
    test_find_ext_files()
