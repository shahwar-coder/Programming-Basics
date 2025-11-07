'''
Q1. What does the enumerate() function do in Python?
Ans:
`enumerate(iterable, start=0)` returns an **iterator** that produces pairs  
of (index, element) while looping through any iterable.
'''
# Example
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry



'''
Q2. Why use enumerate() instead of range(len(...)) ?
Ans:
✅ `enumerate()` is **cleaner and safer**:
- Works with any iterable (not just lists)
- Avoids index errors
- Improves readability

❌ `range(len(...))` is less readable and error-prone.
'''
# Example
# Old way (not recommended)
for i in range(len(fruits)):
    print(i, fruits[i])

# Better way
for i, f in enumerate(fruits):
    print(i, f)



'''
Q3. What is the syntax of enumerate()?
Ans:
enumerate(iterable, start=0)

Parameters:
- iterable → the sequence (list, tuple, string, etc.)
- start → optional index to start counting from (default = 0)
'''
# Example
nums = [10, 20, 30]
for index, value in enumerate(nums, start=1):
    print(index, value)
# 1 10
# 2 20
# 3 30



'''
Q4. What type of object does enumerate() return?
Ans:
It returns an **enumerate object** (an iterator), not a list.  
You can convert it to a list or tuple if needed.
'''
# Example
nums = [10, 20, 30]
print(enumerate(nums))         # <enumerate object at ...>
print(list(enumerate(nums)))   # [(0, 10), (1, 20), (2, 30)]
print(tuple(enumerate(nums)))  # ((0, 10), (1, 20), (2, 30))



'''
Q5. Can enumerate() start from a custom index?
Ans:
Yes — use the `start` parameter to set the starting index.
'''
# Example
names = ["Ali", "Zara", "Hamid"]
for index, name in enumerate(names, start=100):
    print(index, name)
# 100 Ali
# 101 Zara
# 102 Hamid



'''
Q6. Does enumerate() modify the original sequence?
Ans:
❌ No — it only provides an iterator for iteration;  
the original iterable remains **unchanged**.
'''
# Example
nums = [1, 2, 3]
for i, n in enumerate(nums):
    print(i, n)
print(nums)   # [1, 2, 3]



'''
Q7. Can enumerate() be used with strings and tuples?
Ans:
✅ Yes — it works with any iterable (string, list, tuple, range, etc.).
'''
# Example
for i, ch in enumerate("Python"):
    print(i, ch)
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n



'''
Q8. What is the time complexity of enumerate()?
Ans:
Creating an enumerate object → **O(1)**  
Iterating through it → **O(n)**  
It’s efficient since it yields one item at a time (lazy evaluation).
'''
# Example
nums = [10, 20, 30]

# Creating enumerate object → O(1)
enum_obj = enumerate(nums)
print(enum_obj)     # <enumerate object at ...>

# Iterating through it → O(n)
for i, val in enum_obj:
    print(i, val)

# Output:
# 0 10
# 1 20
# 2 30

