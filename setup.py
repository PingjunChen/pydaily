# -*- coding: utf-8 -*-

import os, sys
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="pydaily",
    version=VERSION,
    packages=find_packages(),
    author="Pingjun Chen",
    author_email="chenpingjun@gmx.com",
    description=("Python utility functions ", ),
    license="Apache",
    keywords=["python", "utility functions", "data science",
              "biomedical image analysis", "artificial intelligence"],
    url="https://github.com/PingjunChen/py_utils")
