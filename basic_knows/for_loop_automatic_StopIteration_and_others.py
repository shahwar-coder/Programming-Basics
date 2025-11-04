'''
Q. What exceptions can occur inside a for loop?
Ans:
- `TypeError` → if the object isn’t iterable.  
- `StopIteration` → raised internally when the iterator ends (handled automatically).  
- Any runtime error in the loop body is propagated normally.
'''
# Example
try:
    for x in 1234:    # not iterable
        print(x)
except TypeError as e:
    print("Error:", e)
