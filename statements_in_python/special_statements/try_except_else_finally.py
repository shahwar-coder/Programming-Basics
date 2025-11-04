'''
Q1. What is the main purpose of try/except in Python?
Ans:
It’s used to handle runtime errors gracefully.  
Instead of crashing, Python runs the except block when an error occurs.
'''
# Example
try:
    x = int("ten")
except ValueError:
    print("Invalid number!")
# Output: Invalid number!



'''
Q2. What is the structure of try/except/else/finally blocks?
Ans:
Structure:
try → code that might fail  
except → handles specific errors  
else → runs if no error occurs  
finally → always runs (cleanup or closing actions)
'''
# Example
try:
    x = int("10")
except ValueError:
    print("Error!")
else:
    print("Success!")
finally:
    print("Done")
# Output: Success! \n Done



'''
Q3. What happens if no exception occurs in the try block?
Ans:
Python skips the `except` block, executes the `else` block (if present),  
and then always runs the `finally` block.
'''
# Example
try:
    print("Everything is fine.")
except:
    print("Error caught.")
else:
    print("No errors detected.")
finally:
    print("Always runs.")



'''
Q4. What’s the purpose of the finally block?
Ans:
`finally` always executes, whether or not an exception occurs.  
It’s perfect for cleanup tasks — like closing files or releasing resources.
'''
# Example
try:
    f = open("data.txt")
    print("File opened.")
except FileNotFoundError:
    print("File missing.")
finally:
    print("Closing file (if open).")



'''
Q5. What are the benefits of using try/except over error-prone code?
Ans:
- Prevents program crashes.  
- Lets you respond to errors with custom logic.  
- Keeps code readable, safe, and robust.
'''
# Example
try:
    balance = 100
    withdraw = 200
    if withdraw > balance:
        raise ValueError("Insufficient funds")
except ValueError as e:
    print("Error:", e)



'''
Q6. Can one try block have multiple excepts?
Ans:
Yes! You can handle different error types separately for precise control.
'''
# Example
try:
    val = int(input("Enter number: "))
    print(10 / val)
except ValueError:
    print("Not a valid integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")



'''
Q7. What if the exception type doesn’t match any except block?
Ans:
The error propagates upward — the program stops unless caught elsewhere.
'''
# Example
try:
    print(10 / 0)
except ValueError:
    print("Wrong type!")   # Won’t catch ZeroDivisionError
# → program stops with ZeroDivisionError



'''
Q8. What happens if an exception occurs inside finally?
Ans:
If finally raises a new error, it *overrides* any earlier exception.  
So it’s best to avoid risky operations inside finally.
'''



'''
Q9. How can we catch all exceptions safely?
Ans:
Use a generic `except Exception as e:` —  
but avoid bare `except:` since it also catches system-exiting events.
'''
# Example
try:
    risky_func()
except Exception as e:
    print("Something went wrong:", e)



'''
Q10. Why should you not overuse exceptions for control flow?
Ans:
Because they’re slower and make logic harder to read.  
Use them for *unexpected* situations, not normal program flow.
'''
# Example
# ❌ Avoid this:
try:
    x = my_dict["key"]
except KeyError:
    x = None
# ✅ Better:
x = my_dict.get("key")



'''
Q11. What’s the order of execution when all blocks are present?
Ans:
try → (error?) → except (if any) → else (if no error) → finally (always).
'''
# Example
try:
    print("Try")
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")
# Output: Try → Else → Finally
