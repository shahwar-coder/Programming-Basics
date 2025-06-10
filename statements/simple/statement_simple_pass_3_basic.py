'''
✅ Silence the Syntax Error
What will be the output of the following code?

```python
for i in range(3):
    pass
print("Loop completed")
```
Why doesn't it throw any error even though the for loop has no body?
'''

for i in range(3):
    pass
print("Loop completed")

# Output : Loop completed
# It will not throw any error as pass acts as a temporary replacement doing nothing and just saving from syntax error if it were to be empty.
