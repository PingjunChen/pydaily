# Auxilary


## Execute test scripts in subpackages
```
# Execute test script 'test_file.py' in filesystem subpackage
$ python -m pydaily.filesystem.tests.test_file
```

## Auto Generate requirements.txt
```
$ pip install pipreqs
$ pipreqs $PROJ_PATH
$ pip install -r requirements.txt
```

## Generate coverage report
```
$ pytest --cov=./
$ codecov --token=********
```

## Submit package to PyPI
```
$ rm -rf build dist *.egg-info
$ python setup.py sdist bdist_wheel
$ twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
or $ python3 -m twine upload dist/*
```
