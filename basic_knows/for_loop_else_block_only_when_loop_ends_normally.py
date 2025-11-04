'''
Q. Can you use else with for loops?
Ans:
Yes! The `else` block runs **only if the loop ends normally**,  
not if it’s broken with `break`.
'''
# Example
for n in [1, 2, 3]:
    if n == 4:
        break
else:
    print("Loop completed without break")   # runs
