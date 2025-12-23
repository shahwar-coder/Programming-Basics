# 🔒 Revision
# Tuples = immutable + fixed-size
# Safer & faster than lists
# Hashable → usable as dict keys
# Single element tuple needs a comma

'''
Q1. What is tuple packing?
Ans. Tuple packing means putting multiple values into a tuple automatically.
'''
# Example
t = 1, 2, 3
# Python packs these values into a tuple → t = (1, 2, 3)


'''
Q2. What is tuple unpacking?
Ans. Tuple unpacking means assigning tuple values to multiple variables in one step.
'''
# Example
t = (1, 2, 3)
a, b, c = t
# a = 1, b = 2, c = 3


'''
Q3. What happens if the number of variables doesn’t match the tuple size?
Ans. Python raises an error because it cannot match values correctly.
'''
# Example
t = (1, 2, 3)
# a, b = t    ❌ ValueError (too many values)


'''
Q4. What does the `*rest` syntax mean in unpacking?
Ans. `*rest` collects the remaining values into a list.
'''
# Example
t = (1, 2, 3, 4)
a, *rest = t
# a = 1
# rest = [2, 3, 4]


'''
Q5. Can `*rest` appear in the middle of unpacking?
Ans. Yes. It will capture all values between the fixed variables.
'''
# Example
t = (1, 2, 3, 4, 5)
a, *mid, b = t
# a = 1
# mid = [2, 3, 4]
# b = 5


'''
Q6. What is tuple unpacking used for variable swapping?
Ans. It swaps values cleanly without a temporary variable.
'''
# Example
x = 10
y = 20
x, y = y, x
# x = 20, y = 10


'''
Q7. Why is tuple unpacking considered Pythonic?
Ans. Because it is clear, concise, and avoids extra code.
'''
# Example
# Instead of using temp variables, unpacking does it in one line.


'''
Q8. What is the one-line rule to remember?
Ans. Packing groups values into a tuple; unpacking spreads them into variables.
'''
# Example (lock it 🔒)
# values → tuple → variables
