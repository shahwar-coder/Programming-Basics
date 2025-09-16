'''
Q1. What is the purpose of the assert statement in Python?
Ans: It checks that a condition is True during runtime.  
If False, it raises AssertionError (optionally with a message).  

Example:
'''

x = 5
assert x > 0   # passes silently
assert x < 0, "x must be negative"   # AssertionError: x must be negative



'''
Q2. What happens when you run Python with the -O (optimize) flag?
Ans: All assert statements are stripped out (ignored).  
Therefore, you should not use assert for critical runtime checks.  

Example:
'''
# python -O script.py → assert lines won’t run at all




'''
Q3. What are typical use cases for assert?
Ans:
- Debugging
- Sanity checks
- Validating invariants in development/testing  

Example:
'''
def divide(a, b):
    assert b != 0, "Denominator must not be zero"
    return a / b



'''
Q4. (Coding)
# Predict the outputs
'''
def check_age(age):
    assert age >= 18, "Must be at least 18"
    return "Access granted"

print(check_age(20))
print(check_age(15))

'''
Actual Output:
Access granted
Traceback (most recent call last):
  ...
AssertionError: Must be at least 18
'''


'''
Explanation:
- check_age(20) → condition True → function returns "Access granted".
- check_age(15) → condition False → AssertionError raised with message.
- The exception interrupts execution, so nothing is returned or printed after that.
'''


