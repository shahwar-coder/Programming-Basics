'''
Code Snippet power to check if the string can be converted to number or not
'''

def is_convertible_to_number(text: str)->bool:
  try:
    float(text)
    return True
  except ValueError:
    return False


# STRONGER defense will be :

import math
def is_convertible_to_number(text: str) -> bool:
    try:
        return math.isfinite(float(text)) # here we have extra , use of 'isfinite' for floats because 'nan' , 'inf' etc are also float (we learned this already)
    except ValueError:
        return False
