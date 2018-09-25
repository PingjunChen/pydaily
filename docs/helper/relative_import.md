Fix “Attempted relative import in non-package”
========

### Use repo as package
```
# Execute test script 'test_file.py' in filesystem subpackage
$ python -m pydaily.filesystem.tests.test_file
```


**References**
* [How to fix “Attempted relative import in non-package” even with __init__.py](
    https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py)
