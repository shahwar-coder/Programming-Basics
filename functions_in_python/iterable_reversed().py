'''
Q1. What does the reversed() function do in Python?
Ans:
`reversed(seq)` returns an **iterator** that yields elements of a sequence in **reverse order**.  
It does **not modify** the original sequence.
'''
# Example
nums = [1, 2, 3, 4]
rev = reversed(nums)
print(list(rev))     # [4, 3, 2, 1]
print(nums)          # [1, 2, 3, 4] (unchanged)



'''
Q2. What types of objects can reversed() work on?
Ans:
It works on **sequence types** that support both `__len__()` and `__getitem__()`:
✅ Strings  
✅ Tuples  
✅ Lists  
✅ Range objects  
❌ Sets and Dicts (unordered)
'''
# Example
print(list(reversed("Python")))   # ['n', 'o', 'h', 't', 'y', 'P']
print(tuple(reversed((1, 2, 3)))) # (3, 2, 1)
print(list(reversed(range(5))))   # [4, 3, 2, 1, 0]



'''
Q3. Does reversed() return a list?
Ans:
No — it returns a **reverse iterator**, not a list.  
To see the reversed elements, you can use `list()`, `tuple()`, or a loop.
'''
# Example
nums = [10, 20, 30]
rev = reversed(nums)
print(rev)              # <list_reverseiterator object at ...>
print(list(rev))        # [30, 20, 10]



'''
Q4. How is reversed() different from slicing with [::-1] ?
Ans:
| Feature | reversed(seq) | seq[::-1] |
|----------|----------------|------------|
| Return Type | Iterator | New list/string |
| Memory Use | Low (lazy) | High (copies data) |
| Mutability | Does not copy | Creates copy |
| Works On | Sequences only | Works on any sequence |

✅ Use `reversed()` for efficiency (especially large sequences).  
✅ Use `[::-1]` when you explicitly need a reversed **copy**.
'''
# Example
lst = [1, 2, 3, 4]
print(list(reversed(lst)))  # [4, 3, 2, 1]
print(lst[::-1])            # [4, 3, 2, 1]



'''
Q5. How can you iterate over elements in reverse using reversed()?
Ans:
You can directly use `for ... in reversed(seq)` in a loop.
'''
# Example
for ch in reversed("HELLO"):
    print(ch, end=" ")   # O L L E H



'''
Q6. What happens if reversed() is used on an unordered type like set or dict?
Ans:
It raises a **TypeError**, because sets and dictionaries don’t have a defined order.
'''
# Example
# reversed({1, 2, 3})  # ❌ TypeError
# reversed({'a': 1, 'b': 2})  # ❌ TypeError



'''
Q7. Can you reverse a dictionary’s keys or items using reversed()?
Ans:
Not directly, but you can convert keys/items into a list first.
'''
# Example
d = {'a': 1, 'b': 2, 'c': 3}
print(list(reversed(list(d.items()))))  
# [('c', 3), ('b', 2), ('a', 1)]



'''
Q8. What is the time complexity of reversed()?
Ans:
- Creating the iterator → **O(1)**  
- Iterating fully → **O(n)** (depends on number of elements)  
It’s efficient since it doesn’t copy the sequence.
'''


'''
Q9. Summary:
Ans:
✅ Returns a reverse **iterator** (not a list).  
✅ Works with **sequences** only (strings, lists, tuples, range).  
✅ Does **not modify** the original sequence.  
✅ More **memory-efficient** than slicing `[::-1]`.  
✅ Use `list()`, `tuple()`, or loop to consume it.
'''

