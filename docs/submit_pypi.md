How to submit a package to PyPI
========

### What is PyPI?
```
PyPI — the Python Package Index
The Python Package Index is a repository of software for the Python programming language.
```

### Upload to PyPI
```
$ python setup.py sdist upload -r pypi
$ rm -rf build
$ python setup.py sdist bdist_wheel
$ twine upload -r test --sign dist/pydaily*
```

#### References
* [Getting Started With setuptools and setup.py](https://pythonhosted.org/an_example_pypi_project/setuptools.html)
* [How to submit a package to PyPI](http://peterdowns.com/posts/first-time-with-pypi.html)
* [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty)
