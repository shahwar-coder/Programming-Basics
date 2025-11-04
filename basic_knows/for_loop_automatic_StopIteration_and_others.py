'''
Q. What exceptions can occur inside a for loop?
Ans:
- `TypeError` → if the object isn’t iterable.  
- `StopIteration` → raised internally when the iterator ends (handled automatically).  
- Any runtime error in the loop body is propagated normally.
'''
# Example (TypeError)
try:
    for x in 1234:    # not iterable
        print(x)
except TypeError as e:
    print("Error:", e)

# ======================================================================================

# Example (Automatic Stop Iteration)
for n in nums:
    print(n)
# automatically ends after last item (no visible StopIteration)
