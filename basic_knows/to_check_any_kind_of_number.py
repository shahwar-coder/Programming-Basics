'''
To check if the input is any kind of number (float, int etc) and not any other type
'''

import numbers

def is_number(value):
    return isinstance(value, numbers.Number)
