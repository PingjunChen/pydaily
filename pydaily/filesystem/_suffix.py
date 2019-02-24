# -*- coding: utf-8 -*-

__all__ = ['is_image_file',
           ]


def is_image_file(filename):
    """ Check if given file is image file or not

    Parameters
    -------
    filename: str
        input file path

    Returns
    -------
    img_flag: bool
        flag for image

    """

    IMG_EXTENSIONS = [
        '.jpg', '.JPG', '.jpeg', '.JPEG',
        '.png', '.PNG',
        '.ppm', '.PPM',
        '.bmp', '.BMP',
        'tif', 'TIF', 'tiff', 'TIFF',
    ]

    img_flag = any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

    return img_flag
