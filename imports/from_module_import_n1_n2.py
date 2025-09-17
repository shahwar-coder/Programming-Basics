'''
Q1. What does from module import name1, name2 do in Python?
Ans: It loads the whole module but only binds the chosen names 
into the current namespace, so you can use them directly 
without prefixing with module name.

Example:
'''
from math import sqrt, pi
print(sqrt(9))   # 3.0
print(pi)        # 3.14159...




'''
Q2. What is the main advantage and disadvantage of this style?
Ans:
- Advantage: Less typing, more readable for frequently used functions.
- Disadvantage: Higher risk of name clashes and it can be harder 
  to trace where a function came from in large projects.

Example:
'''
from math import sqrt
from cmath import sqrt   # ❌ overwrites math.sqrt
print(sqrt(-1))          # now cmath.sqrt is active




'''
Q3. What is the best practice when using this import style?
Ans: 
- Use it when you need only a few specific names.
- Always list them explicitly.
- Avoid from module import * (which pollutes namespace).
'''




'''
Q4. (Coding)
# Predict the outputs
'''
from math import sqrt, pi

print("Square root of 16:", sqrt(16))
# ✅ 4.0

print("Value of pi:", pi)
# ✅ 3.141592653589793

import math
print("Compare sqrt functions:", sqrt is math.sqrt)
# ✅ True

'''
Explanation:
- sqrt(16) → 4.0 because we imported sqrt directly.
- pi → 3.141592653589793 (full precision constant from math).
- sqrt is math.sqrt → True, since from-import just binds the same function object 
  into the current namespace.
'''
