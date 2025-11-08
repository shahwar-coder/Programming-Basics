'''
Q1. What is a lambda function in Python?
Ans:
A **lambda function** is a small, anonymous function defined with the `lambda` keyword.  
It can have any number of arguments but only **one expression**, which is automatically returned.
'''
# Example
add_ten = lambda a: a + 10
print(add_ten(5))   # 15


'''
Q2. What is the syntax of a lambda function?
Ans:
Syntax:  
    lambda arguments : expression  
It works just like a one-line function — no `def`, no `return` keyword.
'''
# Example
multiply = lambda a, b: a * b
print(multiply(5, 6))  # 30


'''
Q3. What makes lambda functions different from normal functions?
Ans:
| Feature      | lambda                | def                        |
|------------  |---------------------- |----------------------------|
| **Name**     | Anonymous             | Has name                   |
| **Body**     | Single expression     | Multiple statements        |
| **Return**   | Implicit              | Explicit (`return`)        |
| **Use case** | Short, inline logic   | Full reusable functions    |
'''
# Example
add = lambda x, y: x + y
def add_func(x, y): return x + y
print(add(2, 3), add_func(2, 3))  # 5 5


'''
Q4. When are lambda functions most useful?
Ans:
They’re used when a **small, throwaway function** is needed —  
especially in functions like `map()`, `filter()`, or `sorted()`’s `key` argument.
'''
# Example
nums = [5, 1, 8, 3]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [25, 1, 64, 9]


'''
Q5. Can lambda functions take multiple arguments?
Ans:
Yes, they can — but still must contain **only one expression**.
'''
# Example
add_three = lambda a, b, c: a + b + c
print(add_three(5, 6, 2))  # 13


'''
Q6. Can a lambda function contain statements or assignments?
Ans:
No — only **expressions** are allowed.  
Statements like `for`, `while`, `if-else`, `return`, or `print` can’t appear directly.
'''
# Example (invalid)
# lambda x: for i in x: print(i)  ❌ SyntaxError


'''
Q7. How do you use conditional expressions in lambda?
Ans:
You can use **inline if–else expressions** inside lambda.
'''
# Example
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(5))   # Odd
print(check(8))   # Even


'''
Q8. Can lambda functions be nested or returned from other functions?
Ans:
Yes — they’re often used as **function factories** or callbacks.
'''
# Example
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
print(double(5))   # 10


'''
Q9. Can lambda functions access variables outside their scope?
Ans:
Yes — they **capture variables** from the enclosing scope (like closures).
'''
# Example
n = 5
multiply = lambda x: x * n
print(multiply(3))   # 15
