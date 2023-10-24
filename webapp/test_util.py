import pytest # pip install pytest


def str_to_bool(val):
    '''
    Convert string representation of truth to True or False.
    True values are 'y', 'yes', or ''; case-insensitive.
    False values are 'n' or 'no'; case-insensitive.
    Raise ValueError if 'val' is anything else.
    '''
    true_vals = ['y', 'yes', '']
    false_vals = ['n', 'no']
    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError("invalid truth value %r" % (val))

# create a list of values fot testing True values from the str_to_bool function


true_vals = ['y', 'yes', '']

# create a list of values fot testing False values from the str_to_bool func

false_vals = ['n', 'no']

# use pytest to generate some tests for the str_to_bool function


@pytest.mark.parametrize("input,expected", [
    ('y', True),
    ('yes', True),
    ('', True),
    ('n', False),
    ('no', False),
    ('foo', pytest.raises(ValueError)),
])
def test_str_to_bool(input, expected):
    if isinstance(expected, bool):
        assert str_to_bool(input) == expected
    else:
        with expected:
            str_to_bool(input)

# use parametrize to test the str_to_bool function with a list of inputs for
# True values
@pytest.mark.parametrize("input", ['y', 'yes', ''])
def test_str_to_bool_true(input):
    assert str_to_bool(input) is True
