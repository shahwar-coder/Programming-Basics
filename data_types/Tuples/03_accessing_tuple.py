'''
Q1. How do you access elements in a tuple using indexing?
Ans. You use index positions, just like lists. Indexing starts from 0.
'''
# Example
t = (10, 20, 30)
# t[0] → 10
# t[1] → 20
# t[-1] → 30


'''
Q2. Can tuples be sliced like lists?
Ans. Yes. Slicing works exactly the same way as with lists.
'''
# Example
t = (1, 2, 3, 4, 5)
# t[1:4] → (2, 3, 4)
# t[:3]  → (1, 2, 3)
# t[::2] → (1, 3, 5)


'''
Q3. How do you iterate over a tuple?
Ans. You can loop over a tuple using a for-loop, just like a list.
'''
# Example
t = ("a", "b", "c")
for item in t:
    print(item)


'''
Q4. Can you use indexing inside a loop with tuples?
Ans. Yes. You can iterate using index positions if needed.
'''
# Example
t = (100, 200, 300)
for i in range(len(t)):
    print(t[i])


'''
Q5. What is membership testing in tuples?
Ans. Membership testing checks whether a value exists in the tuple.
'''
# Example
t = (5, 10, 15)
# 10 in t  → True
# 20 in t  → False


'''
Q6. Is membership testing fast in tuples?
Ans. Yes. It is efficient and works the same way as in lists.
'''
# Example
# Python checks each element until it finds a match.


'''
Q7. What is the key difference when accessing tuples vs lists?
Ans. Access is the same, but tuples cannot be modified after access.
'''
# Example
# t[0] = 99 ❌ Error (tuples are immutable)


'''
Q8. What is the one-line rule to remember?
Ans. Tuples support indexing, slicing, iteration, and membership just like lists.
'''
# Example (lock it 🔒)
# Access = same as list
# Modification = NOT allowed
