# -*- coding: utf-8 -*-

import os, sys
import json

__all__ = ['json_to_dict',
           'dict_to_json'
           ]


def json_to_dict(json_path):
    """ Load json file as dictionary.

    """

    with open(json_path) as fp:
        data_dict = json.load(fp)

    return data_dict


def dict_to_json(data_dict, json_path):
    """ Save dictionary to json file.

    """

    with open(json_path, 'w') as fp:
        json.dump(data_dict, fp)
