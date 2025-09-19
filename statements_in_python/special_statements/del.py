'''
Q1. What does the `del` statement do in Python?
Ans: It removes a binding (name, item, slice, or attribute).  
It doesn’t always delete the object itself, just the reference.  

Example:
'''

x = 10
del x
# print(x)  # ❌ NameError: name 'x' is not defined


'''
Q2. How can `del` be used with sequences (lists/slices)? Show examples.
Ans:
- Deleting by index: lst = [1,2,3]; del lst[1] → [1,3]  
- Deleting a slice: nums = [1,2,3,4]; del nums[1:3] → [1,4]
'''

lst = [1,2,3]; del lst[1] → [1,3]  
nums = [1,2,3,4]; del nums[1:3] → [1,4]



'''
Q3. Can `del` delete multiple names at once? Show an example.
Ans: Yes.  
a, b = 1, 2
del a, b
# Now both a and b are undefined.
'''

a, b = 1, 2
del a, b
# Now both a and b are undefined.



'''
Q4. What are common pitfalls of using `del`?
Ans:
- NameError if deleting an undefined name.  
- IndexError if list index is out of range.  
- KeyError if dict key does not exist.  
- Removing the last reference may free the object, 
  but if other references exist, the object stays alive.
'''


'''
Q5. (Coding)
# Predict the outputs
'''

nums = [10, 20, 30, 40]
del nums[2]
print("After index delete:", nums)
# ✅ [10, 20, 40]
# Reason: element at index 2 (value 30) is removed.

del nums[1:3]
print("After slice delete:", nums)
# ✅ [10]
# Reason: slice nums[1:3] → [20, 40] gets deleted in one go.

a = 100
b = a
del a
print("b after del a:", b)
# ✅ 100
# Reason: del a removes only the name 'a'. 
# The object 100 still exists because 'b' also references it.




