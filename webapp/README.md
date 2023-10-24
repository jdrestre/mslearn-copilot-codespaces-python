# Documentation for the str_to_bool function
The str_to_bool function converts a string to a boolean value. It is used to convert the string values of the environment variables to boolean values.

It accepts a string as an argument and returns a boolean value. The function returns `True` if the string is `yes`, `y`, or if it is empty. Otherwise, it returns False.
The function is defined in the `webapp/utils.py` file.

## Usage
```python
from webapp.utils import str_to_bool

str_to_bool('yes') # returns True
str_to_bool('y') # returns True
str_to_bool('') # returns True
str_to_bool('no') # returns False
str_to_bool('n') # returns False
```

## Testing
The function is tested in the `webapp/tests/test_utils.py` file.
```
$ python manage.py test webapp.tests.test_utils
```

## Contributing guidelines
If you want to contribute to the project, you can read the [contributing guidelines](CONTRIBUTING.md).
```
$ git clone
$ cd webapp
$ pip install -r requirements.txt
```
