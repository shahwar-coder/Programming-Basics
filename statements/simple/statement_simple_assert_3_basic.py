'''
✅ Debugging an Assertion
You are given a buggy piece of code:

value = -3
assert value >= 0, "value should be non-negative"
print("Computation continues...")

Task:
What happens when this code is run?
How would you fix the code so it runs without error, assuming negative values are not allowed?
'''

value = -3
assert value >= 0, "value should be non-negative"
print("Computation continues...")

# When the code runs, AssersionError will arise, and "value should be non-negative" will be printed.
# To fix the code, we need to simply pass any value which is not negative.

# Final Summary:
'''
# Assertion is used to ensure assumptions hold true during development.
# If `value` is negative, the assertion fails and raises an AssertionError with the provided message.
# To prevent the error, use a non-negative value.
'''
