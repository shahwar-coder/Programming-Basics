'''
Q1. What is the main difference between lists and tuples?
Ans. Lists are mutable (can change), while tuples are immutable (cannot change).
'''
# Example
lst = [1, 2, 3]
lst.append(4)      # ✅ allowed

tup = (1, 2, 3)
# tup.append(4)    ❌ error (tuples cannot change)


'''
Q2. What does “mutable” mean for lists?
Ans. Mutable means you can add, remove, or modify elements after creation.
'''
# Example
lst = [10, 20, 30]
lst[0] = 99
# lst = [99, 20, 30]


'''
Q3. What does “immutable” mean for tuples?
Ans. Immutable means once created, the tuple’s elements cannot be changed.
'''
# Example
tup = (10, 20, 30)
# tup[0] = 99 ❌ not allowed


'''
Q4. Why are lists called dynamic?
Ans. Because their size can grow or shrink during runtime.
'''
# Example
lst = []
lst.append(1)
lst.append(2)
# Size keeps changing dynamically


'''
Q5. Why are tuples called fixed-size?
Ans. Because their size is decided at creation and cannot be changed later.
'''
# Example
tup = (1, 2, 3)
# Always length = 3

# Tuples are called fixed-size because their length is decided at creation
# and cannot be changed later.

# If you try to add or modify elements, Python does NOT change the
# original tuple. Instead, it creates a completely new tuple.

# The original tuple always remains the same.


'''
Q6. When should you use a list?
Ans. Use a list when data needs to change over time.
'''
# Example
shopping_cart = ["apple", "banana"]
shopping_cart.append("orange")


'''
Q7. When should you use a tuple?
Ans. Use a tuple when data should stay constant and protected.
'''
# Example
RGB_COLOR = (255, 0, 0)


'''
Q8. What is the one-line rule to remember?
Ans. Lists are mutable and dynamic; tuples are immutable and fixed.
'''
# Example (lock it 🔒)
# Changeable data → list
# Fixed data → tuple
