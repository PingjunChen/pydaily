# -*- coding: utf-8 -*-

import os, sys, pdb
from pydaily.filesystem import batch_rename_files
from pydaily import DATA_DIR

def test_batch_rename_files():
    input_dir = os.path.join(DATA_DIR, 'input/thyroid/thumb_slide')
    save_dir = os.path.join(DATA_DIR, 'output')
    batch_rename_files(input_dir, save_dir, start_num=5)


if __name__ == '__main__':
    test_batch_rename_files()
