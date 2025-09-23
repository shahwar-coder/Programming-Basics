'''
Q1. Does Python have a ternary operator like C/Java?
Ans:
- No traditional `?:`.
- Instead, Python uses a conditional expression:
  value_if_true if condition else value_if_false

Q2. How does ternary differ from normal if-else statements?
Ans:
- Ternary is an expression (returns value).
- if-else statement just controls flow.
'''
x = 7
# Statement version
if x%2==0:
    result = "Even"
else:
    result = "Odd"

# Ternary expression version
result2 = "Even" if x%2==0 else "Odd" #python's conditional expression (instead of ternary), (more readable)

print(result, result2)
