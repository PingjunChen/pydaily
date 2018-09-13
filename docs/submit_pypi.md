How to submit a package to PyPI
========

### What is PyPI?
```
PyPI — the Python Package Index
The Python Package Index is a repository of software for the Python programming language.
```

### Upload to PyPI
```
$ rm -rf build dist *.egg-info
$ python setup.py sdist bdist_wheel
$ twine upload --repository-url https://upload.pypi.org/legacy/ dist/
```

#### References
* [Getting Started With setuptools and setup.py](https://pythonhosted.org/an_example_pypi_project/setuptools.html)
* [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty)
