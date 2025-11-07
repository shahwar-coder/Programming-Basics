'''
Q. Can list comprehension be used for side effects (like printing)?
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
