# -*- coding: utf-8 -*-

import os, sys
import glob, shutil

__all__ = ['batch_rename_files',
           ]

def batch_rename_files(input_dir, save_dir, ext='.png', start_num=0, filename_len=5):
    all_files = glob.glob(os.path.join(input_dir, "*" + ext))

    # Delete out directory and create a new one
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.makedirs(save_dir)

    # print("---Start renaming---")
    for ind, filepath in enumerate(all_files):
        cur_ind = start_num + ind
        save_filename = str(cur_ind).zfill(filename_len) + ext
        save_path = os.path.join(save_dir, save_filename)
        shutil.copy(filepath, save_path)
    # print("---Renaming finished---")
