'''
Q1. Why would you use import module as alias in Python?
Ans: To shorten long module names, follow community conventions, 
or avoid naming conflicts.

Example:
'''
import numpy as np
print(np.array([1, 2, 3]))




'''
Q2. Does aliasing create a new copy of the module?
Ans: No. Alias is just another reference to the same module object.

Example:
'''
import math as m
import math
print(id(m), id(math))   # same id




'''
Q3. What are common alias conventions in Python?
Ans:
- numpy → np
- pandas → pd
- matplotlib.pyplot → plt
These improve readability and are widely recognized.
'''




'''
Q4. (Coding)
# Predict the outputs
'''
import math as m
print("m.sqrt(16):", m.sqrt(16))

import math
print("math.sqrt(25):", math.sqrt(25))

print("Same object?", id(m) == id(math))


'''
Actual Output:
import math as m
print("m.sqrt(16):", m.sqrt(16))
# ✅ 4.0

import math
print("math.sqrt(25):", math.sqrt(25))
# ✅ 5.0

print("Same object?", id(m) == id(math))
# ✅ True
'''

'''
Explanation:
- m is just an alias (another name) for the math module.
- math and m both point to the same module object in memory.
- That’s why the IDs are identical and the final comparison is True.
'''
