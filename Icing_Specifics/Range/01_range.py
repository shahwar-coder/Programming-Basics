'''
Q1. What does the range() function return?
Ans:
range() returns an immutable sequence of numbers.  
It does NOT create a list; it creates a lightweight range object that
generates numbers on demand.
'''
# Example
r = range(5)
print(r)          # range(0, 5)
print(list(r))    # [0, 1, 2, 3, 4]


'''
Q2. How does basic range(n) work?
Ans:
With one argument, range(n) generates numbers from 0 to n-1.
'''
# Example
for x in range(5):
    print(x)   # 0,1,2,3,4


'''
Q3. What do start, stop, and step mean in range(start, stop, step)?
Ans:
start = first number (inclusive)  
stop  = end number (exclusive)  
step  = step size (default = 1)
'''
# Example
print(list(range(3, 10, 2)))  # [3, 5, 7, 9]


'''
Q4. Can range() count backwards?
Ans:
Yes. Use a negative step to count down.
'''
# Example
print(list(range(10, 3, -2)))   # [10, 8, 6, 4]


'''
Q5. What makes range() memory-efficient?
Ans:
range() stores only: start, stop, step.  
It does NOT store all numbers in memory.
Even huge ranges use tiny memory.
'''
# Example
import sys
print(sys.getsizeof(range(1_000_000_000)))  # very small


'''
Q6. How do you slice a range?
Ans:
Slicing a range returns another optimized range object.
'''
# Example
r = range(10)
print(r[:4])          # range(0, 4)
print(list(r[:4]))    # [0, 1, 2, 3]


'''
Q7. How does membership checking work in range()?
Ans:
"x in range(a,b,step)" is O(1).  
Python mathematically checks if x fits the pattern—no iteration.
'''
# Example
print(6 in range(0, 10, 2))  # True
print(7 in range(0, 10, 2))  # False


'''
Q8. What happens if step is 0?
Ans:
range(..., step=0) raises ValueError because the sequence cannot advance.
'''
# Example
# range(5, 10, 0)  # ValueError


'''
Q9. Are ranges comparable or equal?
Ans:
Yes. Two ranges are equal if they would produce the same sequence.
'''
# Example
print(range(0,10,2) == range(0,11,2))  # True


'''
Q10. Does a range object support indexing and len()?
Ans:
Yes. range supports:
• indexing → r[i]  
• slicing  → r[a:b]  
• len(r)   → number of items
'''
# Example
r = range(0, 10, 2)
print(r[2])   # 4
print(len(r)) # 5 elements


'''
Q11. Why is range() preferred in loops?
Ans:
Because it:
• uses constant memory  
• is faster  
• avoids building large lists  
• is clean and Pythonic
'''
# Example
for i in range(1_000_000):
    pass
