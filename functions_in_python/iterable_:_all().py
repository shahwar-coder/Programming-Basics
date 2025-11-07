'''
Q1. What does all(iterable) do?
Ans:
It returns **True** if *all elements* in the iterable are truthy.  
If *any element* is falsy, it returns **False**.
'''
# Example
print(all([1, 2, 3]))      # True (all truthy)
print(all([1, 0, 3]))      # False (0 is falsy)



'''
Q2. How does all() treat empty iterables?
Ans:
For an **empty iterable**, `all()` returns **True**.  
This follows the principle of *vacuous truth* —  
no element violates the condition.
'''
# Example
print(all([]))      # True
print(all(()))      # True



'''
Q3. What kinds of iterables work with all()?
Ans:
It works with **any iterable** — lists, tuples, sets, dicts, generators, etc.  
For dictionaries, it checks the **keys**.
'''
# Example
print(all((1, 2, 3)))           # True
print(all({1, 2, 0}))           # False
print(all({"a": 1, "b": 0}))    # True (keys are non-empty strings)



'''
Q4. How does all() decide if something is truthy or falsy?
Ans:
It internally calls `bool()` on each element:  
- Truthy → continues checking  
- Falsy → stops early (short-circuit evaluation)
'''
# Example
print(all(["yes", 5, [1]]))  # True
print(all(["", 5, [1]]))     # False ('' is falsy)



'''
5.
Example Code:
==> Check if all numbers in a list are even.
'''
# Example
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # True (all even)



'''
Q6. How does short-circuiting work in all()?
Ans:
`all()` stops checking as soon as it finds the first falsy value —  
making it efficient for large datasets.
'''
# Example
def check(x):
    print("Checking:", x)
    return x > 0

print(all(check(i) for i in [1, 2, -3, 4]))  
# Stops at -3



'''
Q7. What’s the difference between all() and any()?
Ans:
- `all()` → True if *every* element is truthy  
- `any()` → True if *at least one* element is truthy  
They are logical opposites in behavior.
'''
# Example
print(all([1, 0, 3]))   # False
print(any([1, 0, 3]))   # True



'''
Q8. How can you use all() with generators?
Ans:
You can pair it with generator expressions for memory-efficient checks.
'''
# Example
nums = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in nums))  # True

