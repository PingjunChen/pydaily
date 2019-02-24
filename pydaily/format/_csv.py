# -*- coding: utf-8 -*-

import pandas as pd

__all__ = ['csv_to_dict',
           'dict_to_csv'
           ]

def csv_to_dict(csv_path):
    """ Load csv to python dictionary.

    Parameters
    -------
    csv_path: str
        csv file path

    Returns
    -------
    data_dict: dict
        data represented as python dictionary

    """

    df = pd.read_csv(csv_path)
    data_dict = df.to_dict('list')

    return data_dict


def dict_to_csv(data_dict, csv_path):
    """ Save python dictionary to csv file.

    Parameters
    -------
    data_dict: dict
        data represented as dictionary
    csv_path: str
        csv file path to save

    """

    df = pd.DataFrame.from_dict(data_dict)
    df.to_csv(csv_path, index=False)
