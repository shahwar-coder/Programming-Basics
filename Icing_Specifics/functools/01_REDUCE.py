# ============================================================
# reduce() in Python — concise but detailed
# ============================================================

# reduce() repeatedly COMBINES elements into a single value
# It lives in functools
from functools import reduce

# Syntax:
#   reduce(function, iterable[, initializer])
# - function takes TWO arguments (accumulator, current)
# - iterable is list, tuple, etc.
# - result is a SINGLE value (not an iterator)

# ------------------------------------------------------------
# 1. Basic example: sum of numbers
numbers = [1, 2, 3, 4]

total = reduce(lambda acc, x: acc + x, numbers)
# Step-by-step:
# acc=1, x=2 → 3
# acc=3, x=3 → 6
# acc=6, x=4 → 10
# Result: 10

# ------------------------------------------------------------
# 2. Multiply all elements
product = reduce(lambda acc, x: acc * x, numbers)
# Result: 24

# ------------------------------------------------------------
# 3. Find maximum value
max_value = reduce(lambda a, b: a if a > b else b, numbers)
# Result: 4

# ------------------------------------------------------------
# 4. Using initializer (VERY important nuance)
# initializer is the starting value of accumulator
sum_with_init = reduce(lambda acc, x: acc + x, numbers, 10)
# Calculation: 10 + 1 + 2 + 3 + 4
# Result: 20

# ------------------------------------------------------------
# 5. Reduce with strings (concatenation)
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda a, b: a + b, words)
# Result: "Hello World!"

# ------------------------------------------------------------
# 6. Reduce with dictionaries (merge dicts)
dicts = [
    {"a": 1},
    {"b": 2},
    {"c": 3}
]
merged = reduce(lambda acc, d: {**acc, **d}, dicts)
# Result: {'a': 1, 'b': 2, 'c': 3}

# ------------------------------------------------------------
# 7. map vs filter vs reduce (clear distinction)
nums = [1, 2, 3, 4]

mapped = list(map(lambda x: x * 2, nums))            # transforms → [2,4,6,8]
filtered = list(filter(lambda x: x % 2 == 0, nums))  # selects → [2,4]
reduced = reduce(lambda a, b: a + b, nums)           # combines → 10

# ------------------------------------------------------------
# 8. Common real-world pattern (pipeline)
# Sum of squares of even numbers
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))
)
# Steps:
# filter → [2,4]
# map → [4,16]
# reduce → 20

# ------------------------------------------------------------
# 9. When to use reduce()
# ✔ When final result must be ONE value
# ✔ Custom aggregation logic
# ✔ Functional pipelines
# ❌ Avoid for simple sum(), max(), min() (built-ins are clearer)

# ------------------------------------------------------------
# 10. Mental model
# reduce asks:
# “How do I combine everything into ONE thing?”
