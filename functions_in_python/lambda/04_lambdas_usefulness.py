'''
Q1. What are some common scenarios where lambda is ideal?
Ans:
✅ Best suited for:
- Inline operations with `map()`, `filter()`, or `sorted()`  
- Tiny helper functions inside larger expressions  
- One-time computations or short transformations
'''


'''
✅ 1️⃣ Inline operations with map(), filter(), or sorted()
Lambda is perfect when you just need a quick one-line transformation or filtering,
without defining a full `def` function.
'''
# map() → Apply quick transformation
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]

# filter() → Select items based on condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)     # [2, 4]

# sorted() → Sort using custom rule (descending by length)
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w), reverse=True)
print(sorted_words)  # ['banana', 'cherry', 'apple', 'pie']

# ===================================================================

'''
✅ 2️⃣ Tiny helper functions inside larger expressions
Lambda is handy when defining **inline logic** passed into another function,
especially for data processing, GUI callbacks, or small computations.
'''
# Example: find maximum by absolute value
nums = [-10, 5, -3, 8]
max_val = max(nums, key=lambda x: abs(x))
print(max_val)  # -10 (largest absolute value)

# Example: Quick transformation before printing
print(list(map(lambda name: name.title(), ["ali", "zara", "hamid"])))
# ['Ali', 'Zara', 'Hamid']

# Example: Sorting students by grade percentage
students = [("Ali", 85), ("Zara", 92), ("Hamid", 78)]
top_student = max(students, key=lambda s: s[1])
print(top_student)  # ('Zara', 92)


# ===================================================================


'''
✅ 3️⃣ One-time computations or short transformations
Lambda shines for **temporary logic** — when you need a quick computation
inside a loop, return, or comprehension, without creating a separate named function.
'''
# Example: Inline square root rounding
import math
nums = [2, 3, 5, 7]
roots = [ (lambda x: round(math.sqrt(x), 2))(x) for x in nums ]
print(roots)  # [1.41, 1.73, 2.24, 2.65]

# Example: Used once for conditional logic
values = [10, -5, 0, 8]
signs = list(map(lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero"), values))
print(signs)
# ['Positive', 'Negative', 'Zero', 'Positive']

# Example: In a dictionary sorting by computed metric
products = {"apple": 50, "banana": 30, "mango": 80}
sorted_by_discount = sorted(products.items(), key=lambda x: x[1] * 0.9)  # assuming 10% off
print(sorted_by_discount)
# [('banana', 30), ('apple', 50), ('mango', 80)]



'''
Q2. When should you avoid using lambda functions?
Ans:
❌ Avoid lambdas when:
- Logic spans multiple steps  
- You need loops, conditionals, or error handling  
- The function is reused or needs clarity  
(Use `def` instead.)
'''
# Example (better with def)
# ❌ unreadable
process = lambda x: (x + 2) * 3 if x > 0 else -x / 2

# ✅ cleaner with def
def process(x):
    if x > 0:
        return (x + 2) * 3
    else:
        return -x / 2



'''
Q3. Are lambdas always faster than def functions?
Ans:
Not really — lambdas are **syntactic shortcuts**, not performance boosters.  
They run just as fast as equivalent `def` functions.
'''
