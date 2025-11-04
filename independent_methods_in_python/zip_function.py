'''
Q1. What does Python’s zip() function do?
Ans:
It combines elements from two or more iterables (like lists or tuples)  
into tuples, pairing items with the same index.  
It stops when the shortest iterable ends.
'''
# Example
names = ["Ali", "Sara", "Omar"]
scores = [85, 90, 88]
result = list(zip(names, scores))
print(result)    # [('Ali', 85), ('Sara', 90), ('Omar', 88)]



'''
Q2. What is the syntax of the zip() function?
Ans:
Syntax → `zip(iterable1, iterable2, ...)`  
It can take two or more iterables and returns a *zip object* (an iterator).
'''



'''
Q3. What kind of object does zip() return?
Ans:
It returns a *zip object*, which is an iterator.  
To see its contents, convert it using `list()` or `tuple()`.
'''
# Example
z = zip([1, 2], [3, 4])
print(z)             # <zip object at ...>
print(list(z))       # [(1, 3), (2, 4)]



'''
Q4. How does zip() behave when iterables have different lengths?
Ans:
It stops at the shortest iterable — extra elements in longer ones are ignored.
'''
# Example
a = [1, 2, 3]
b = ["x", "y"]
print(list(zip(a, b)))    # [(1, 'x'), (2, 'y')]



'''
Q5. What are some common uses of zip()?
Ans:
- Pairing related data (like names and scores)  
- Looping through multiple lists together  
- Unzipping data using the * operator
'''



'''
Q6. How can you unzip paired data created by zip()?
Ans:
Use the unpacking operator `*` to unzip back into separate iterables.
'''
# Example
pairs = [('Ali', 85), ('Sara', 90)]
names, scores = zip(*pairs)
print(names)   # ('Ali', 'Sara')
print(scores)  # (85, 90)



'''
Q7. Does zip() create a new list in memory?
Ans:
No — it returns a *lazy iterator*.  
Data isn’t stored in memory until you explicitly convert it (e.g., with list()).
'''
# Example
z = zip(range(1000000), range(1000000))
# Memory efficient — doesn't build a huge list



'''
Q8. What happens if one of the iterables is empty?
Ans:
The result is an empty iterator — because zip stops as soon as the shortest iterable ends.
'''
# Example
print(list(zip([], [1, 2, 3])))   # []



'''
Q9. Can zip() be used with more than two iterables?
Ans:
Yes! You can combine any number of iterables —  
each tuple in the result will have one element from each iterable.
'''
# Example
a = [1, 2]
b = ['x', 'y']
c = [True, False]
print(list(zip(a, b, c)))  # [(1, 'x', True), (2, 'y', False)]



'''
Q10. What exception should you be aware of with zip()?
Ans:
zip() itself doesn’t raise exceptions during iteration,  
but if you try to unpack into fewer or more variables than zipped values,  
you’ll get a `ValueError`.
'''
# Example
for x, y in zip([1, 2], [3]):  # second list shorter
    print(x, y)   # works fine, but no second pair

# ❌ Mismatch unpacking
try:
    for x, y, z in zip([1, 2], [3, 4]):
        pass
except ValueError as e:
    print("Error:", e)



'''
Q11. Why is zip() often preferred in data processing?
Ans:
It allows *parallel iteration* in a clean, memory-efficient way  
— perfect for pairing columns, combining records, or merging datasets.
'''
# Example
fields = ["Name", "Age"]
values = ["Alice", 25]
print(dict(zip(fields, values)))   # {'Name': 'Alice', 'Age': 25}
