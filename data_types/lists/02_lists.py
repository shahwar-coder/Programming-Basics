'''
Q1. How do you access individual elements in a list?
Ans:
You use **indexing** — `lst[i]` gives the element at position `i`.  
Indexing starts from **0** (first item) and supports **negative indices** for reverse access.
'''
# Example
lst = [10, 20, 30, 40]
print(lst[0])    # 10  (first element)
print(lst[-1])   # 40  (last element)



'''
Q2. What happens if you access an index that doesn’t exist?
Ans:
Python raises an **IndexError** because the position is out of range.
'''
# Example
lst = [1, 2, 3]
# print(lst[5])  → IndexError: list index out of range



'''
Q3. What is slicing and how is it done?
Ans:
Slicing extracts **sub-parts** of a list using the form  
`lst[start:end:step]`.  
It creates a **new list** and doesn’t modify the original.
'''
# Example
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])     # [1, 2, 3]
print(nums[:3])      # [0, 1, 2]
print(nums[::2])     # [0, 2, 4]



'''
Q4. How do you access elements inside nested lists?
Ans:
Use **multiple indexes** — each bracket `[ ]` goes one level deeper.
'''
# Example
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])   # 3 (row 1, column 0)



'''
Q5. What is the purpose of membership operators in lists?
Ans:
`in` and `not in` check whether a value exists inside a list.  
They return `True` or `False`.
'''
# Example
lst = [10, 20, 30]
print(20 in lst)       # True
print(50 not in lst)   # True



'''
Q6. What happens when slicing goes beyond list boundaries?
Ans:
Python **doesn’t raise an error** —  
it safely adjusts the range and returns valid elements only.
'''
# Example
lst = [1, 2, 3]
print(lst[0:10])   # [1, 2, 3]



'''
Q7. What does a negative step in slicing do?
Ans:
A negative step reverses the direction — often used to **reverse lists**.
'''
# Example
nums = [1, 2, 3, 4]
print(nums[::-1])   # [4, 3, 2, 1]



'''
Q8. Are membership checks (x in lst) fast?
Ans:
No — `in` performs a **linear search** in lists → O(n).  
For faster membership checks, use **sets**, which provide **O(1)** average time lookup.
'''

# Example with list (slow for large data)
lst = [1, 2, 3, 4, 5]
print(5 in lst)        # True (checks each element)
print(100 in lst)      # False (scans all elements)

# Example with set (much faster for lookups)
s = {1, 2, 3, 4, 5}
print(5 in s)          # True (hash lookup, O(1))
print(100 in s)        # False (immediate check)

# Demonstration for large collections
large_list = list(range(1_000_000))
large_set = set(range(1_000_000))

# Checking membership
print(999_999 in large_list)   # Slower → linear scan
print(999_999 in large_set)    # Faster → constant time

# Summary:
# - `in` with **list/tuple** → O(n) time (linear search)
# - `in` with **set/dict** → O(1) average time (hash-based lookup)
# - Prefer sets when frequent membership testing is required.




'''
Q9. Can slicing be used to copy lists?
Ans:
Yes — using `lst[:]` creates a **shallow copy** of the list.
'''
# Example
a = [1, 2, 3]
b = a[:]        # copy
b.append(4)
print(a, b)     # [1, 2, 3] [1, 2, 3, 4]
