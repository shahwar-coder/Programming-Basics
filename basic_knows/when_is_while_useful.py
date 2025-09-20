'''
Q4. How does a while loop work?
Ans:
- Repeats until condition is False.
- Useful when number of iterations unknown.

Example:
'''
x = 3
while x > 0:
    print(x)
    x -= 1

# Step-by-step:
# 1. x=3 → prints 3 → x=2
# 2. x=2 → prints 2 → x=1
# 3. x=1 → prints 1 → x=0 → loop ends.
