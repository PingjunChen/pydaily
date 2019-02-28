# -*- coding: utf-8 -*-

import deepdish as dd

__all__ = ['h5_to_dict',
           'dict_to_h5'
           ]

def h5_to_dict(h5_path):
    """ Load h5 to python dictionary.

    Parameters
    -------
    h5_path: str
        h5 file path

    Returns
    -------
    data_dict: dict
        data represented as python dictionary

    """

    data_dict = dd.io.load(h5_path)

    return data_dict


def dict_to_h5(data_dict, h5_path):
    """ Save python dictionary to h5 file.

    Parameters
    -------
    data_dict: dict
        data represented as dictionary
    h5_path: str
        h5 file path to save

    """

    dd.io.save(h5_path, data_dict)
