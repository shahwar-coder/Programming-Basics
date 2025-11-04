'''
Q1. What is the main purpose of a while loop in Python?
Ans:
A while loop repeats a block of code as long as a given condition is True.  
It’s ideal when the number of iterations isn’t known in advance.
'''
# Example
count = 0
while count < 3:
    print(count)
    count += 1
# Output: 0 1 2



'''
Q3. How do you create an infinite loop intentionally?
Ans:
Use `while True:` — it runs forever until you break it manually using `break`.
'''
# Example
while True:
    name = input("Enter name (or 'q' to quit): ")
    if name == 'q':
        break



'''
Q4. What are typical uses of while loops?
Ans:
- Repeated user input until valid  
- Waiting for an event or condition  
- Running until a target state is reached  
- Iterations when count is unknown
'''
# Example
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted!")




'''
Q5. How is while different from for?
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
Q6. What should you be careful about when using while loops?
Ans:
Always ensure the condition eventually becomes False.  
If not, you’ll create an **infinite loop** that never ends.
'''
# Example
# ❌ Wrong — count never changes
# while count < 5:
#     print(count)
#
# ✅ Fix:
count = 0
while count < 5:
    print(count)
    count += 1



'''
Q7. Can while loops use an else clause?
Ans:
Yes! The `else` block runs if the loop ends normally  
(not if it exits early using `break`).
'''
# Example
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished without break")



'''
Q8. When is a while loop better than a for loop?
Ans:
When you don’t know how many times to loop —  
for example, waiting for user input or an external event.
'''
# Example
while True:
    cmd = input("Command: ")
    if cmd == "exit":
        break
    print("You entered:", cmd)



'''
Q9. Why might a while loop be slower than a for loop?
Ans:
Because while checks a condition at every step  
and doesn’t leverage iterator protocols —  
it’s more flexible, but slightly less optimized for simple iteration.
'''
# Example
# while = dynamic condition check each time
# for = optimized iterator traversal
