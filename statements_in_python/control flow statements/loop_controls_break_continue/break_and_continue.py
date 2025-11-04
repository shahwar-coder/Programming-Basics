'''
Q1. What is the purpose of loop control statements in Python?
Ans:
They modify the normal flow of loops.  
`break` and `continue` let you stop or skip iterations as needed.
'''



'''
Q2. What does the break statement do?
Ans:
`break` immediately exits the current loop —  
it stops all remaining iterations, even if the condition is still True.
'''
# Example
for x in range(5):
    if x == 3:
        break
    print(x)
# Output: 0 1 2




'''
Q3. What does the continue statement do?
Ans:
`continue` skips the rest of the current loop iteration  
and moves directly to the next one.
'''
# Example
for x in range(5):
    if x % 2 == 0:
        continue
    print(x)
# Output: 1 3



'''
Q4. How do break and continue differ?
Ans:
- `break` → exits the loop entirely.  
- `continue` → skips to the next iteration but keeps the loop running.
'''
# Example
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
# Output: 0 1 3



'''
Q5. In which loops can we use break and continue?
Ans:
Both can be used in *for* and *while* loops —  
and even inside nested loops (affecting only the innermost one).
'''
# Example
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
# Output: (0,0), (1,0), (2,0)



'''
Q6. What are common use cases for break and continue?
Ans:
- `break`: stop when a target or condition is met.  
- `continue`: skip unwanted items while filtering data.
'''
# Example
nums = [1, -2, 3, -4, 5]
for n in nums:
    if n < 0:
        continue    # skip negatives
    print("Positive:", n)



'''
Q7. Can break and continue be used with else in loops?
Ans:
Yes!  
If a loop ends normally (not via `break`), the `else` block runs.  
If `break` occurs, the `else` block is skipped.
'''



'''
Q8. What happens if break or continue appear outside a loop?
Ans:
Python raises a `SyntaxError` —  
they must be inside a `for` or `while` loop.
'''
# Example
# ❌ Invalid:
# break
# → SyntaxError: 'break' outside loop




'''
Q9. Can break and continue be used with try/except inside loops?
Ans:
Yes, but if the loop body raises an exception before reaching them,  
the break/continue won’t execute — the exception is handled first.
'''
# Example
for x in [1, 0, 2]:
    try:
        print(10 // x)
    except ZeroDivisionError:
        continue    # skips division by zero
# Output: 10 5
