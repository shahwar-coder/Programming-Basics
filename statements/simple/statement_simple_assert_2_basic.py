'''
✅ Assertion Behavior
What will be the output of the following code?

x = 10
assert x > 5
print("Assertion passed!")

assert x < 5, "x must be less than 5"
print("This line prints?")
'''

x = 10
assert x > 5
print("Assertion passed!")

assert x < 5, "x must be less than 5"
print("This line prints?")

# Output: First "Assertion passed!" will be printed as x>5 is 10>5 (True)
# Then : AssertionError will be thrown, as x is not less than 5.
# And : "This line prints?" WON'T BE PRINTED.

# Notes:
'''
- assert is used to catch logical errors early.
- If the condition fails, AssertionError is raised.
- Optional error messages help clarify the failure.
- Execution stops immediately at the point of failure.
'''
