'''
📌 Exception Chaining in Python

1. Implicit chaining
• Happens automatically when new exception is raised in an except block
• Stored in __context__

2. Explicit chaining (raise ... from ...)
• raise NewExc from OldExc
• Sets __cause__ explicitly
• Clearer error tracebacks

3. Suppressing chaining
• raise NewExc from None
• Removes context → cleaner output

🔑 Use chaining to make error causes explicit & debuggable
'''




'''
Q1. What is implicit exception chaining in Python?
Ans: If a new exception is raised inside an except block, 
the original exception is stored in __context__ automatically.

Example:
'''
try:
    1/0
except ZeroDivisionError:
    raise ValueError("Bad math")

# ValueError raised, ZeroDivisionError stored in __context__




'''
Q2. What is explicit exception chaining? How is it different?
Ans: Use `raise NewExc from OldExc` to set the cause explicitly.  
It shows in the traceback with "The above exception was the direct cause of...".

Example:
'''
try:
    1/0
except ZeroDivisionError as e:
    raise ValueError("Bad math") from e




'''
Q3. How do you suppress exception chaining?
Ans: Use `raise ... from None`. This removes the context and shows 
only the new exception in the traceback.

Example:
'''

try:
    1/0
except ZeroDivisionError:
    raise ValueError("Bad math") from None




'''
Q4. Why use explicit chaining instead of implicit?
Ans: Explicit chaining makes the error relationship clearer, 
avoids confusion in tracebacks, and improves debugging.
'''



'''
Q5. (Coding)
# Predict what happens
'''

def f():
    try:
        int("x")
    except ValueError as e:
        raise TypeError("Conversion failed") from e

f()

'''
Traceback (most recent call last):
  File "...", line X, in f
    int("x")
ValueError: invalid literal for int() with base 10: 'x'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "...", line Y, in <module>
    f()
  File "...", line X, in f
    raise TypeError("Conversion failed") from e
TypeError: Conversion failed
'''

'''
Explanation:
- The first exception (ValueError) is shown.
- Then Python prints "The above exception was the direct cause of the following exception".
- Then it shows the second exception (TypeError).
'''
