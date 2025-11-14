'''
Q1. What is the purpose of try/except in Python?
Ans:
try/except lets you handle errors gracefully. Code inside try may fail,
and except runs only when an exception occurs.
'''
# Example
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")



'''
Q2. Why is it important to catch specific exceptions?
Ans:
Catching specific errors (like ValueError, TypeError) avoids hiding
unexpected bugs and helps diagnose real issues easily.
'''
# Example
try:
    int("abc")
except ValueError:
    print("Invalid number!")



'''
Q3. What is the role of the else block in exception handling?
Ans:
The else block runs ONLY when no exception happens in the try block.
Useful for code that should execute only after successful operations.
'''
# Example
try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Conversion successful!")  # runs only if no error



'''
Q4. What does the finally block do?
Ans:
finally runs ALWAYS — whether an exception occurs or not.
It is used for cleanup operations like closing files or connections.
'''
# Example
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File missing")
finally:
    print("Done (cleanup here)")



'''
Q5. How do you raise your own exception?
Ans:
Use raise to manually create and trigger an exception when a condition
is invalid or unsafe.
'''
# Example
value = -5
if value < 0:
    raise ValueError("Value must be non-negative!")



'''
Q6. What are best practices for exception handling?
Ans:
- Catch specific exceptions
- Keep try small
- Avoid silent except: blocks
- Use finally for cleanup
- Use raise to enforce constraints
'''
# Example
try:
    n = int("123")
except ValueError:
    print("Invalid integer!")



'''
Q7. Why should you avoid except: without specifying an error?
Ans:
It catches EVERYTHING—including unexpected bugs like NameError or SyntaxError.
This can hide real problems and make debugging hard.
'''
# Example
# BAD:
# try:
#     risky()
# except:
#     pass    # hides all errors



'''
Q8. Can you catch multiple exceptions in one except block?
Ans:
Yes. Pass a tuple of exceptions to handle several related errors.
'''
# Example
try:
    n = int("abc")
except (ValueError, TypeError):
    print("Conversion error")



'''
Q9. What happens if an exception is raised inside finally?
Ans:
If finally raises an exception, it overrides any previous exception.
Use it carefully and avoid raising new errors inside finally blocks.
'''
# Example
try:
    1 / 0
finally:
    print("Finally runs even during crash!")



'''
Q10. What is the difference between raising and re-raising an exception?
Ans:
raise Exception(...) creates a new exception.
raise (with no arguments) re-throws the current exception to be handled elsewhere.
'''
# Example 1: Logging + re-raise (common use case)
def process():
    try:
        int("abc")
    except ValueError as e:
        print("Log: Invalid integer input!")
        raise   # re-raises the SAME ValueError
process()  
# Output:
# Log: Invalid integer input!
# then traceback of ValueError

# =================================

# Example 2: Cleanup + re-raise
def connect():
    try:
        print("Opening file...")
        f = open("no_such_file.txt")
    except FileNotFoundError:
        print("Cleanup: closing resources or undoing steps...")
        raise   # still let caller know the file was missing

try:
    connect()
except FileNotFoundError:
    print("Caller: I will handle it now.")
