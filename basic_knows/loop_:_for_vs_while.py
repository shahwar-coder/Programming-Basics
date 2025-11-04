'''
Q. How is while different from for?
Ans:
- `for` → *data-driven* (iterates over items in a sequence).  
- `while` → *condition-driven* (runs until condition becomes False).
'''
# Example
for i in range(3):      # data-driven
    print(i)

count = 0
while count < 3:        # condition-driven
    print(count)
    count += 1
