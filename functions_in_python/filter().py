# ============================================================
# filter() in Python — concise but detailed
# ============================================================

# filter() selects elements from an iterable based on a condition
# Syntax:
#   filter(function, iterable)
# - function must return True or False
# - iterable can be list, tuple, set, etc.
# - result is an iterator → convert to list if needed

# ------------------------------------------------------------
# 1. Basic example: keep even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6]

# ------------------------------------------------------------
# 2. Filter positive numbers
nums = [-3, -1, 0, 2, 5]
positives = list(filter(lambda x: x > 0, nums))
# Result: [2, 5]

# ------------------------------------------------------------
# 3. Filter strings by length
words = ["hi", "hello", "cat", "python"]
long_words = list(filter(lambda w: len(w) > 3, words))
# Result: ['hello', 'python']

# ------------------------------------------------------------
# 4. Filter strings by condition (starts with capital letter)
names = ["Rahul", "shahwar", "Amit", "john"]
capital_names = list(filter(lambda n: n[0].isupper(), names))
# Result: ['Rahul', 'Amit']

# ------------------------------------------------------------
# 5. Filter dictionaries by key value
employees = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 22},
    {"name": "Bob", "age": 35}
]
senior_employees = list(filter(lambda e: e["age"] > 25, employees))
# Keeps full dicts where condition is True

# ------------------------------------------------------------
# 6. filter() returns an iterator (important nuance)
result = filter(lambda x: x > 0, nums)
# print(result)  # <filter object ...>
print(list(result))  # convert to list to see values

# ------------------------------------------------------------
# 7. Using filter(None, iterable)
# Removes all falsy values: 0, "", None, False
values = [0, 1, "", "hi", None, 5]
truthy_values = list(filter(None, values))
# Result: [1, 'hi', 5]

# ------------------------------------------------------------
# 8. filter() vs map()
# - filter(): selects elements
# - map(): transforms elements
mapped = list(map(lambda x: x * 2, numbers))        # transforms
filtered = list(filter(lambda x: x % 2 == 0, numbers))  # selects

# ------------------------------------------------------------
# 9. filter + map together (functional pipeline)
# Step 1: filter positives
# Step 2: double them
pipeline = list(
    map(lambda x: x * 2, filter(lambda x: x > 0, nums))
)
# Result: [4, 10]

# ------------------------------------------------------------
# 10. When to use filter()
# ✔ Short, clear conditions
# ✔ Functional pipelines
# ✔ Streaming / iterator-based data
# ❌ For readability, list comprehension is often preferred:
#     [x for x in nums if x > 0]
