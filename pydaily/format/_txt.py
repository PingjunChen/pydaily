# -*- coding: utf-8 -*-

__all__ = ['txt_to_list',
           'list_to_txt'
           ]

def txt_to_list(txt_path):
    """ Load text file as list

    Parameters
    -------
    txt_path: str
        text file path

    Returns
    -------
    data_list: list
        data represented as python list

    """

    with open(txt_path, 'r') as file:
      data_list = [line.rstrip('\n') for line in file]

    return data_list


def list_to_txt(data_list, txt_path):
    """ Save python list to text file

    Parameters
    -------
    data_list: list
        data represented as python list
    txt_path: str
        text file path to save

    """

    with open(txt_path, 'w') as file:
        for item in data_list:
            file.write("{}\n".format(item))
