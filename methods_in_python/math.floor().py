'''
Q1. What does math.floor(x) do?
Ans:
It returns the **largest integer less than or equal to x** —  
that is, it always **rounds down** toward negative infinity.
'''
# Example
import math
print(math.floor(5.9))   # 5
print(math.floor(5.1))   # 5



'''
Q2. How does math.floor() behave with negative numbers?
Ans:
It still rounds **downward**, meaning toward negative infinity.  
So `math.floor(-3.2)` → `-4`, and `math.floor(-7.9)` → `-8`.
'''
# Example
import math
print(math.floor(-3.2))  # -4
print(math.floor(-7.9))  # -8



'''
Q3. What type of value does math.floor(x) return?
Ans:
It always returns an **integer**, even when the input is a float.
'''
# Example
import math
x = math.floor(9.9)
print(x, type(x))   # 9 <class 'int'>



'''
Q4. How does math.floor() differ from math.ceil() and int()?
Ans:
- `math.floor(x)` → rounds **down** (toward −∞)  
- `math.ceil(x)` → rounds **up** (toward +∞)  
- `int(x)` → truncates (toward 0)
'''
# Example
import math
x = -3.7
print(math.floor(x))  # -4
print(math.ceil(x))   # -3
print(int(x))         # -3



'''
Q5. How does math.floor() behave with infinity or NaN?
Ans:
- `math.floor(math.inf)` → `inf`  
- `math.floor(-math.inf)` → `-inf`  
- `math.floor(math.nan)` → raises `ValueError`
'''
