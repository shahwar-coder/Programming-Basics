'''
Q1. What does reduce() do in simple words?
A.
reduce() takes many values and combines them step by step
to produce ONE final value.
It repeatedly applies a function to accumulate a result.
'''
# Example:
# numbers = [1, 2, 3, 4]
# reduce(lambda a, b: a + b, numbers)
# Step-by-step: ((1+2)+3)+4 = 10


'''
Q2. How is reduce() different from map() and filter()?
A.
map() transforms each element,
filter() selects some elements,
reduce() combines all elements into one value.
'''
# Example:
# nums = [1, 2, 3]
# map → [2, 4, 6]
# filter → [2]
# reduce → 6 (1+2+3)


'''
Q3. Why does reduce() need a function with TWO arguments?
A.
Because reduce() works with:
- an accumulator (current result)
- the next element from the iterable
It combines them repeatedly.
'''
# Example:
# lambda acc, x: acc * x
# acc keeps the running product


'''
Q4. What is the role of the accumulator in reduce()?
A.
The accumulator stores the partial result after each step,
and carries it forward to the next step.
'''
# Example:
# numbers = [2, 3, 4]
# acc=2 → acc=2*3=6 → acc=6*4=24


'''
Q5. What is an initializer in reduce(), and why is it important?
A.
The initializer is the starting value of the accumulator.
It is useful when:
- the iterable may be empty
- you want a custom starting point
'''
# Example:
# reduce(lambda a, b: a + b, [1, 2, 3], 10)
# Calculation: 10+1+2+3 = 16


'''
Q6. When should reduce() be used?
A.
Use reduce() when the final result must be ONE value
and the combination logic is custom or non-trivial.
'''
# Example:
# Finding product of all numbers
# reduce(lambda a, b: a * b, [1, 2, 3, 4]) → 24
