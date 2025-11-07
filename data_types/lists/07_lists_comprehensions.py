'''
Q1. What is list comprehension in Python?
Ans:
List comprehension is a **concise and expressive way** to create lists by looping, filtering, and transforming data — all in one line.
'''
# Example
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]



'''
Q2. What is the syntax of list comprehension?
Ans:
[ expression for item in iterable if condition ]

- `expression`: defines what to compute or transform  
- `iterable`: sequence to loop through  
- `if condition`: (optional) filters items
'''
# Example
nums = [1, 2, 3, 4, 5]
even = [x for x in nums if x % 2 == 0]
print(even)  # [2, 4]



'''
Q3. How can we use functions or expressions in a list comprehension?
Ans:
We can apply **built-in functions** or **operations** on each element in the comprehension.
'''
# Example
words = ["apple", "banana", "cherry"]
upper = [w.upper() for w in words]
lengths = [len(w) for w in words]
print(upper)    # ['APPLE', 'BANANA', 'CHERRY']
print(lengths)  # [5, 6, 6]



'''
Q4. How do you include an if–else condition inside list comprehension?
Ans:
1️⃣ **if–else before the `for`** → used to **choose a value** based on a condition
2️⃣ **if after the `for`** → used to **filter items** (no `else` allowed)  
'''
# ------------------------------------------------------------
# Example 1 – if–else **before** for  → conditional value
# ------------------------------------------------------------
nums = [-2, -1, 0, 1, 2]
result = [x if x > 0 else 0 for x in nums]
print(result)   # [0, 0, 0, 1, 2]

# ------------------------------------------------------------
# Example 2 – if **after** for  → conditional filter
# ------------------------------------------------------------
nums = [-2, -1, 0, 1, 2]
positive = [x for x in nums if x > 0]
print(positive)  # [1, 2]



'''
Q5. How can list comprehensions replace nested loops?
Ans:
We can use multiple `for` clauses in one comprehension to generate pairs or flatten data.
'''
# Example 1: Cartesian pairs
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# Example 2: Flatten nested list
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6]



'''
Q6. How does list comprehension compare to a regular loop?
Ans:
✅ List comprehension:
- Shorter and more readable  
- Often faster (optimized C implementation)  
❌ Regular loop:
- More flexible for complex multi-step logic
'''
# Example
# List comprehension
squares = [x**2 for x in range(5)]

# Traditional loop
squares2 = []
for x in range(5):
    squares2.append(x**2)
print(squares, squares2)



'''
Q7. What’s the difference between an “if filter” and an “if–else expression” in list comprehension?
Ans:
- Filter: `[x for x in lst if x > 0]` → includes only positive elements  
- Expression: `[x if x > 0 else 0 for x in lst]` → transforms each element
'''
# Example
lst = [-2, 0, 3]
print([x for x in lst if x > 0])        # [3]
print([x if x > 0 else 0 for x in lst]) # [0, 0, 3]



'''
Q8. Can list comprehensions work with strings and functions?
Ans:
Yes — they can iterate through characters or apply any callable.
'''
# Example
text = "Python"
chars = [ch for ch in text]
print(chars)  # ['P', 'y', 't', 'h', 'o', 'n']

nums = [3.2, 4.7, 1.5]
rounded = [round(n) for n in nums]
print(rounded)  # [3, 5, 2]



'''
Q9. Are nested comprehensions allowed?
Ans:
Yes, but readability suffers.  
Avoid **too many nested comprehensions** — use loops instead.
'''
# Example (ok)
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]

# Example (avoid)
nested = [[x*y for y in range(3)] for x in range(3)]
print(nested)  # [[0, 1, 2], [0, 2, 4], [0, 3, 6]]



'''
Q10. Can list comprehension be used for side effects (like printing)?
Ans:
It **shouldn’t** — list comprehensions are meant to **create new lists**,  
not for side effects like printing or logging.

Why?
Because the goal of a list comprehension is to **build and return a list**.  
When you use it only for `print()` or similar operations,  
it still **creates an unnecessary list of `None` values** 
(since `print()` returns `None`).

That wastes memory and looks unpythonic.
'''
# Example 1 — ❌ Not recommended
result = [print(x) for x in range(3)]
print("Returned list:", result)

# Output:
# 0
# 1
# 2
# Returned list: [None, None, None]
# (print() executed 3 times, but a useless list of Nones is created)

# Example 2 — ✅ Better and clean
for x in range(3):
    print(x)

# Output:
# 0
# 1
# 2

'''
✅ Explanation:
- In the first case, `[print(x) for x in range(3)]` runs print() for each value,
  but also collects its return value (`None`) in a list → `[None, None, None]`.

- In the second case, a normal `for` loop simply performs the action
  without creating any unnecessary list in memory.

💡 Use comprehensions for building lists — not for actions with no return value.
'''
