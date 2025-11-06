'''
Q1. What does math.fabs(x) do?
Ans:
It returns the **absolute value** of a number as a **float**,  
regardless of whether the input is an int or float.
'''
# Example
import math
print(math.fabs(-5))     # 5.0
print(math.fabs(-3.25))  # 3.25
print(math.fabs(0))      # 0.0



'''
Q2. How is math.fabs(x) different from abs(x)?
Ans:
- `abs(x)` → works for any type (int, float, complex, custom classes).  
- `math.fabs(x)` → works only for **real numbers** and always returns a **float**.
'''
# Example
import math
print(abs(-5))       # 5 (int)
print(math.fabs(-5)) # 5.0 (float)



'''
3.
==>> fabs --> stands for --> "float absolute value"
'''
# Example
import math
values = [-5, -3.2, 7]
result = [math.fabs(x) for x in values]
print(result)  # [5.0, 3.2, 7.0]



'''
Q4. What happens if you pass a boolean or string to math.fabs()?
Ans:
- Booleans are treated as integers (True=1, False=0).  
- Strings cause a `TypeError`.
'''
