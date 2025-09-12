'''
Q1. What is the difference between a normal assignment and an augmented assignment?
Ans: 
- Normal assignment: x = x + y → always creates a new object (for immutables).  
- Augmented assignment: x += y → first tries in-place (__iadd__); 
if unavailable, falls back to normal assignment.

Q2. How does augmented assignment behave differently for mutable vs immutable objects?
Ans: 
- Mutables (list, dict, set): modified in-place, no new object created.  
  Example: nums = [1,2]; nums += [3] → nums becomes [1,2,3], same id.  

- Immutables (int, str, tuple): a new object is created, and the name is rebound.  
  Example: x = 5; x += 2 → x now 7, but id(x) changes (new object).


Q3. Can augmented assignments apply to attributes, items, or slices?
Ans: Yes. Examples:  
- nums[0] += 5  
- obj.attr *= 2  
- nums[1:3] += [7,8]

Q4. (Coding)
# Predict the outputs
'''

# Case 1: Immutable (int)
x = 5
print("id(x) before:", id(x))
x += 2
print("id(x) after:", id(x), "value:", x)

# Case 2: Mutable (list)
nums = [1, 2]
print("id(nums) before:", id(nums), "values:", nums)
nums += [3]
print("id(nums) after:", id(nums), "value:", nums)

# Case 3: Slice assignment
letters = ["a", "b", "c", "d"]
letters[1:3] += ["X", "Y"]
print("After slice augmented assignment:", letters)


'''
# Case 1: Immutable (int)
x = 5
print("id(x) before:", id(x))
x += 2
print("id(x) after:", id(x), "value:", x)

# ✅ Output:
# id(x) before: (some id1)
# id(x) after: (different id2) value: 7
# Reason: ints are immutable → x += 2 creates a NEW int object (7),
# then rebinds x to it. That's why the id changes.

# Case 2: Mutable (list)
nums = [1, 2]
print("id(nums) before:", id(nums), "value:", nums)
nums += [3]
print("id(nums) after:", id(nums), "value:", nums)

# ✅ Output:
# id(nums) before: (id1) value: [1, 2]
# id(nums) after: (same id1) value: [1, 2, 3]
# Reason: lists are mutable → nums += [3] modifies the SAME list in place.
# The id stays the same.

# Case 3: Slice assignment
letters = ["a", "b", "c", "d"]
letters[1:3] += ["X", "Y"]
print("After slice augmented assignment:", letters)

# ✅ Output:
# ['a', 'b', 'c', 'X', 'Y', 'd']
# Reason: letters[1:3] refers to the slice ["b","c"].
# The += extends that slice with ["X","Y"], so new elements are inserted
# in place → list becomes ['a', 'b', 'c', 'X', 'Y', 'd'].
'''
