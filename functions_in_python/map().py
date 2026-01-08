# ============================================================
# map() in Python — concise but detailed
# ============================================================

# map() TRANSFORMS each element of an iterable
# Syntax:
#   map(function, iterable)
# - function takes ONE element and returns a new value
# - iterable can be list, tuple, set, etc.
# - result is an iterator → convert to list if needed

# ------------------------------------------------------------
# 1. Basic example: square each number
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
# Result: [1, 4, 9, 16]

# ------------------------------------------------------------
# 2. Convert strings to uppercase
names = ["rahul", "shahwar", "amit"]
upper_names = list(map(lambda x: x.upper(), names))
# Result: ['RAHUL', 'SHAHWAR', 'AMIT']

# ------------------------------------------------------------
# 3. Get length of each string
words = ["apple", "banana", "kiwi"]
lengths = list(map(lambda w: len(w), words))
# Result: [5, 6, 4]

# ------------------------------------------------------------
# 4. map() with multiple iterables
# map applies function element-wise
a = [1, 2, 3]
b = [10, 20, 30]
summed = list(map(lambda x, y: x + y, a, b))
# Result: [11, 22, 33]

# ------------------------------------------------------------
# 5. map() with dictionaries (transform each dict)
data = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]
# Add a new key without mutating original dict
updated = list(map(lambda x: {**x, "country": "India"}, data))

# ------------------------------------------------------------
# 6. map() returns an iterator (important nuance)
result = map(lambda x: x * 2, numbers)
# print(result)  # <map object ...>
print(list(result))  # convert to list

# ------------------------------------------------------------
# 7. map() vs for-loop
# for-loop version:
doubled_loop = []
for x in numbers:
    doubled_loop.append(x * 2)

# map version:
doubled_map = list(map(lambda x: x * 2, numbers))

# ------------------------------------------------------------
# 8. map() vs list comprehension
# Often more readable:
doubled_lc = [x * 2 for x in numbers]

# Use map() when:
# ✔ transformation is short
# ✔ functional style / pipelines
# ✔ multiple iterables involved

# ------------------------------------------------------------
# 9. map() + filter() together (common pattern)
nums = [-2, -1, 0, 2, 4]
result = list(
    map(lambda x: x * 10, filter(lambda x: x > 0, nums))
)
# Result: [20, 40]

# ------------------------------------------------------------
# 10. Mental model
# map asks:
# “Given x, what should x become?”
