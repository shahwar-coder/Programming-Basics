'''
- elif
- same as 'else if'
- 
```
if condition1:
    # block1
elif condition2:
    # block2
elif condition3:
    # block3
else:
    # fallback block (optional)
```

- how it works? -> simple, checks if first, if false, goes to elif
                -> once matched, it skips remaining blocks
- elif when not used can lead to further checking of remaining conditions even though first one was already True. Therefore inefficient.
'''

# Example:

marks = 82

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

