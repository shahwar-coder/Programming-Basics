'''
Q1. What does math.ceil(x) do?
Ans:
It returns the **smallest integer greater than or equal to x**.  
In other words, it rounds a number **upward** toward positive infinity.
'''
# Example
import math
print(math.ceil(5.1))   # 6
print(math.ceil(5.9))   # 6



'''
Q2. How does math.ceil() behave with negative numbers?
Ans:
For negative values, it still rounds **up toward zero**,  
so `math.ceil(-3.2)` → `-3`, and `math.ceil(-7.9)` → `-7`.
'''
# Example
import math
print(math.ceil(-3.2))  # -3
print(math.ceil(-7.9))  # -7



'''
Q3. What is the return type of math.ceil(x)?
Ans:
It always returns an **integer**, even if the input is a float.
'''
# Example
import math
x = math.ceil(4.2)
print(x, type(x))  # 5 <class 'int'>



'''
Q4. What’s the difference between math.ceil() and math.floor()?
Ans:
- `math.ceil(x)` → rounds **up** to the next integer  
- `math.floor(x)` → rounds **down** to the previous integer
'''
# Example
import math
print(math.ceil(4.2))   # 5
print(math.floor(4.2))  # 4



'''
Q5. How does math.ceil() differ from round()?
Ans:
- `math.ceil()` always rounds **up**  
- `round()` rounds to the **nearest** integer (banker’s rounding)
'''
# Example
import math
print(math.ceil(2.1), round(2.1))  # 3, 2
print(math.ceil(2.9), round(2.9))  # 3, 3



'''
Q8. How does math.ceil() behave with special float values?
Ans:
- `math.ceil(math.inf)` → `inf` (infinite integer type)  
- `math.ceil(-math.inf)` → `-inf`  
- `math.ceil(math.nan)` → raises `ValueError`
'''
