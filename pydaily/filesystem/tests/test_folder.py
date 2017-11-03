# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.filesystem import overwrite_dir
from pydaily import DATA_DIR

def test_overwrite_dir():
    test_dir = os.path.join(DATA_DIR, 'input/TestResults')
    overwrite_dir(test_dir)


if __name__ == '__main__':
    test_overwrite_dir()
