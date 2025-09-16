'''
Q1. What does the raise statement do in Python?
Ans: It triggers an exception. 
If uncaught, the program stops with a traceback.

Example:
'''

raise ValueError("Invalid input")




'''
Q2. How do you re-raise an exception inside an except block?
Ans: Use a bare raise without specifying the exception.

Example:
'''

try:
    1 / 0
except ZeroDivisionError:
    print("Handling...")
    raise   # re-raises ZeroDivisionError



'''
Q3. What must be the type of object you raise?
Ans: It must be an exception instance or class derived from BaseException.

Example:
'''
raise TypeError("Wrong type")
# raise "error"   ❌ invalid (not an exception object)



'''
Q4. How do you create and raise a custom exception?
Ans: Define a subclass of Exception, then raise it.

Example:
'''
class MyError(Exception): pass
raise MyError("Something went wrong")




'''
Q5 Output?
'''
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Caught:", e)

'''
Actual Output:
Caught: Division by zero!
'''

'''
Explanation:
- divide(10, 0) hits the raise statement → ZeroDivisionError("Division by zero!").
- Control jumps to the except block.
- The exception object `e` holds the message string.
- print("Caught:", e) prints → Caught: Division by zero!
'''
