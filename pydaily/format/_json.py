# -*- coding: utf-8 -*-

import json

__all__ = ['json_to_dict',
           'dict_to_json'
           ]


def json_to_dict(json_path):
    """ Load json file as dictionary

    Parameters
    -------
    json_path: str
        json file path

    Returns
    -------
    data_dict: dict
        data represented as python dictionary

    """

    with open(json_path) as fp:
        data_dict = json.load(fp)

    return data_dict


def dict_to_json(data_dict, json_path):
    """ Save dictionary to json file

    Parameters
    -------
    data_dict: dict
        data represented as dictionary
    json_path: str
        json file path to save

    """

    with open(json_path, 'w') as fp:
        json.dump(data_dict, fp)
