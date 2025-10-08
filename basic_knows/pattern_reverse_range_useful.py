'''
Q1. What does range(n, 0, -1) generate?
Ans:
- A reverse sequence starting from n and ending at 1.
- The `stop` value (0) is **exclusive**, so iteration stops before reaching 0.
'''
for i in range(5, 0, -1):
    print(i, end=" ")

# Step-by-step:
# Starts at 5, decrements by 1 → stops before 0 → prints 5 4 3 2 1



'''
Q2. Why is step = -1 used in reverse loops?
Ans:
- `step=-1` tells Python to move backward each iteration.
- Without it, the loop would never run (as start > stop).
'''
# Wrong (won’t run)
for i in range(5, 0):  # default step=+1, 5>0 → no iteration
    print(i)

# Correct
for i in range(5, 0, -1):
    print(i)



'''
Q3. How is reverse range used in pattern problems?
Ans:
- Commonly used when patterns shrink from n → 1.
- Example: reverse triangle or inverted pyramid.
'''
for i in range(5, 0, -1):
    print("*" * i)

# Step-by-step:
# Prints decreasing rows of stars (5 → 1)



'''
Q4. Can reverse range work with custom steps (not -1)?
Ans:
- Yes, any negative step works (e.g., -2 for skipping numbers).
'''
for i in range(10, 0, -2):
    print(i, end=" ")

# Output: 10 8 6 4 2



'''
Q5. How does range differ from reversed(range(...))?
Ans:
- `range(n,0,-1)` explicitly defines reverse iteration.
- `reversed(range(1, n+1))` reverses a forward range.
- Both yield same result, but `reversed()` is more readable sometimes.
'''
print(list(range(5, 0, -1)))          # [5,4,3,2,1]
print(list(reversed(range(1, 6))))    # [5,4,3,2,1]
