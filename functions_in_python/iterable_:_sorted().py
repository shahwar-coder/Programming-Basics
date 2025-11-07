'''
Q1. What does the sorted() function do in Python?
Ans:
`sorted(iterable, *, key=None, reverse=False)`  
creates a **new sorted list** from any iterable, without changing the original.
'''
# Example
nums = [5, 2, 9, 1]
print(sorted(nums))           # [1, 2, 5, 9]
print(nums)                   # [5, 2, 9, 1] (unchanged)



'''
Q2. What types of objects can sorted() work on?
Ans:
It works on **any iterable** — lists, tuples, sets, strings, and even dictionaries.
'''
# Example
print(sorted("python"))       # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted({3, 1, 2}))      # [1, 2, 3]
print(sorted((5, 2, 8)))      # [2, 5, 8]



'''
Q3. How can you sort in descending order using sorted()?
Ans:
Use the `reverse=True` argument to reverse the sorting order.
'''
# Example
nums = [5, 2, 9, 1]
print(sorted(nums, reverse=True))  # [9, 5, 2, 1]



'''
Q4. How does the key parameter work in sorted()?
Ans:
`key` lets you specify a **function** that defines how items are compared.  
For example, sorting by string length or lowercase version.
'''
# Example
words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))          # ['apple', 'banana', 'cherry']
print(sorted(words, key=str.upper))    # ['apple', 'banana', 'cherry']



'''
Q5. What’s the difference between sort() and sorted()?
Ans:
| Feature | sort() | sorted() |
|----------|--------|-----------|
| Works on | Lists only | Any iterable |
| Returns | None | New list |
| Modifies original | ✅ Yes | ❌ No |
| Syntax | `lst.sort()` | `sorted(iterable)` |
'''
# Example
nums = [3, 1, 2]
print(sorted(nums))  # [1, 2, 3]
nums.sort()
print(nums)          # [1, 2, 3] (modified)



'''
Q6. Can sorted() handle mixed data types?
Ans:
No — trying to compare incompatible types (like int and str)  
raises a **TypeError** in Python 3.
'''
# Example
# sorted([1, 'a', 2])  # ❌ TypeError: '<' not supported between instances of 'str' and 'int'



'''
Q7. What happens when you sort a dictionary?
Ans:
Sorting a dictionary returns a list of its **keys**, ordered lexicographically.  
To sort by values, use `key=dict.get`.
'''
# Example
scores = {'Alice': 85, 'Bob': 90, 'Eve': 78}
print(sorted(scores))                 # ['Alice', 'Bob', 'Eve'] (keys)
print(sorted(scores, key=scores.get)) # ['Eve', 'Alice', 'Bob'] (by value)



'''
Q8. Is sorted() stable? What does that mean?
Ans:
Yes — Python’s `sorted()` is **stable**, meaning it preserves  
the order of equal elements based on their original positions.
'''
# Example
data = [('a', 2), ('b', 1), ('c', 2)]
print(sorted(data, key=lambda x: x[1]))
# [('b', 1), ('a', 2), ('c', 2)] → 'a' before 'c' is preserved



'''
Q9. What’s the time complexity of sorted()?
Ans:
Uses **Timsort**, same as list.sort():  
Average and worst case → **O(n log n)**.
'''



'''
Q10. Summary:
Ans:
✅ `sorted()` Highlights  
- Works with all iterables  
- Returns a new sorted list  
- Supports `key` (custom logic) and `reverse=True`  
- Keeps the original unchanged  
🔹 Prefer `sorted()` when immutability or flexibility is needed.
'''
# Example
names = ["Bob", "alice", "Charlie"]
print(sorted(names, key=str.lower))
# ['alice', 'Bob', 'Charlie']
