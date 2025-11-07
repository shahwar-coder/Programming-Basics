'''
Q1. What does “mutable” mean for lists in Python?
Ans:
It means lists can be **changed in place** — you can modify, add, or remove items  
without creating a new list.
'''
# Example
lst = [5, 6, 7, 8]
lst[1] = 10
print(lst)   # [5, 10, 7, 8]



'''
Q2. How do you add elements to a list?
Ans:
You can add items using:
- `append(x)` → adds one element at the **end**
- `extend(iterable)` → adds multiple elements from another iterable
- `insert(index, value)` → adds element at a specific position
'''
# Example
lst = [1, 2, 3]
lst.append(4)        # [1, 2, 3, 4]
lst.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
lst.insert(2, 99)    # [1, 2, 99, 3, 4, 5, 6]
print(lst)



'''
Q3. How can you remove elements from a list?
Ans:
You can remove items using:
- `pop([index])` → removes and returns an element (default: last)
- `remove(value)` → removes the first occurrence of a value
- `del` → deletes by index or slice
- `clear()` → empties the list
'''
# Example
nums = [10, 20, 30, 40]
nums.pop()       # removes 40
nums.remove(20)  # removes first 20
del nums[0]      # deletes 10
print(nums)      # [30]
nums.clear()     # []
print(nums)




'''
Q4. How does extend() differ from append() when adding a list?
Ans:
- `append()` adds the list itself as a single element.  
- `extend()` adds each element from that list individually.
'''
# Example
a = [1, 2]
a.append([3, 4])
print(a)   # [1, 2, [3, 4]]
b = [1, 2]
b.extend([3, 4])
print(b)   # [1, 2, 3, 4]



'''
Q5. Do these operations create a new list?
Ans:
No — all modification methods (`append`, `extend`, `insert`, etc.)  
**change the list in place** and return `None`.
'''
# Example
lst = [1, 2, 3]
result = lst.append(4)
print(lst, result)   # [1, 2, 3, 4] None
