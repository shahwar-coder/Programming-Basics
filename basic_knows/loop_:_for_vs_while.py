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



'''
Q. Why might a while loop be slower than a for loop?
Ans:
Because while checks a condition at every step  
and doesn’t leverage iterator protocols —  
it’s more flexible, but slightly less optimized for simple iteration.
'''
# Example
# while = dynamic condition check each time
# for = optimized iterator traversal
