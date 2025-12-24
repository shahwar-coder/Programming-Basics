'''
Q1. What is a set in Python?
Ans. A set is an unordered collection of unique elements.
'''
# Example
s = {1, 2, 3}
# Elements are unique and order does not matter


'''
Q2. What does “unordered” mean in sets?
Ans. It means elements have no fixed position or index.
'''
# Example
s = {10, 20, 30}
# s[0] ❌ Error (sets do not support indexing)


'''
Q3. What does “unique elements” mean in sets?
Ans. It means a set cannot contain duplicate values.
'''
# Example
s = {1, 2, 2, 3}
# s becomes {1, 2, 3} automatically


'''
Q4. What happens if you try to add duplicates to a set?
Ans. Python silently ignores duplicates.
'''
# Example
s = {1, 2}
s.add(2)
# s is still {1, 2}


'''
Q5. Can sets store elements by position like lists or tuples?
Ans. No. Sets do not support indexing or slicing.
'''
# Example
# s[1] ❌
# s[1:3] ❌


'''
Q6. How do you check if an element exists in a set?
Ans. Use the `in` keyword (very fast).
'''
# Example
s = {5, 10, 15}
# 10 in s → True
# 20 in s → False


'''
Q7. Why are sets useful if they have no order?
Ans. They are great for removing duplicates and fast membership checking.
'''
# Example
nums = [1, 2, 2, 3, 3]
unique_nums = set(nums)
# {1, 2, 3}


'''
Q8. What is the one-line rule to remember?
Ans. A set is an unordered collection of unique elements with no indexing.
'''
# Example (lock it 🔒)
# No order + no duplicates + no index
