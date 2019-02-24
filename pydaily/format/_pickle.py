# -*- coding: utf-8 -*-

import os
import pickle

__all__ = ['pkl_to_dict',
           'dict_to_pkl'
           ]

def pkl_to_dict(pkl_path):
    """ Load pickle file as python dictionary

    Parameters
    -------
    pkl_path: str
        pickle file path

    Returns
    -------
    data_dict: dict
        data represented as python dictionary

    """

    if not os.path.exists(pkl_path):
        raise AssertionError("{} not exist".format(pkl_path))

    with open(pkl_path, 'rb') as handle:
        data_dict = pickle.load(handle)

    return data_dict


def dict_to_pkl(data_dict, pkl_path):
    """ Save dictionary data as pickle file

    Parameters
    -------
    data_dict: dict
        data represented as dictionary
    pkl_path: str
        pickle file path to save

    """

    with open(pkl_path, 'wb') as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
