'''
Q1. What is the main purpose of a for loop in Python?
Ans:
A for loop lets you iterate over elements of any *iterable* —  
like lists, tuples, strings, dictionaries, or ranges.
'''
# Example
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
# apple
# banana
# cherry



'''
Q2. What is the syntax of a for loop?
Ans:
Syntax:
for <variable> in <iterable>:  
  <block of code>  
The loop runs once for every element in the iterable.
'''
# Example
for letter in "hi":
    print(letter)
# h
# i



'''
Q3. How can you use range() in for loops?
Ans:
`range(start, stop, step)` generates a sequence of numbers,  
often used to loop a fixed number of times.
'''
# Example
for i in range(1, 6):
    print(i, end=" ")   # 1 2 3 4 5



'''
Q4. What are enumerate() and zip(), and why are they useful?
Ans:
- `enumerate(iterable)` → gives both index and value.  
- `zip(a, b)` → lets you loop through two or more sequences in parallel.
'''
# Example
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

for i, name in enumerate(names):
    print(i, name)

for name, age in zip(names, ages):
    print(name, "is", age)



'''
Q5. How does a for loop work internally?
Ans:
It first creates an *iterator* using `iter()`.  
Then it keeps calling `next()` to get each element,  
and stops when `StopIteration` is raised.
'''
# Example
nums = [10, 20, 30]
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it) → raises StopIteration




'''
Q6. When should you use a for loop?
Ans:
Use it when you want to go through every element of a sequence or collection,  
especially when the total number of elements is known.
'''
# Example
for i, name in enumerate(["Alice", "Bob", "Charlie"]):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie



'''
Q7. Why is Python’s for loop preferred over a manual counter loop (like in C)?
Ans:
Because it’s *iterator-based*, not index-based —  
it’s simpler, cleaner, and works on any iterable without knowing its length.
'''
# Example
for ch in "Python":
    print(ch, end=" ")   # P y t h o n



'''
Q8. When is a for loop better than a while loop?
Ans:
Use `for` when the number of iterations or iterable is known.  
Use `while` when looping depends on a *condition* that changes dynamically.
'''
# Example
# For → known range
for i in range(5):
    print(i)

# While → unknown duration
count = 0
while count < 5:
    print(count)
    count += 1



'''
Q9. Can for loops work with dictionaries and sets?
Ans:
Yes!  
- With dictionaries → iterate over keys, values, or items.  
- With sets → iterate over unique unordered elements.
'''
# Example
student = {"name": "Ava", "age": 20}
for key, value in student.items():
    print(key, "→", value)

for item in {"red", "blue", "green"}:
    print(item)



'''
Q9. What happens if you modify a list while looping over it?
Ans:
It can cause unexpected behavior because the iterator gets confused.  
Better to loop over a copy using `list[:]` or use list comprehension.
'''
# Example
nums = [1, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)   # Risky
print(nums)   # May skip elements



'''
Q10. Can you use else with for loops?
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



'''
Q11. What exceptions can occur inside a for loop?
Ans:
- `TypeError` → if the object isn’t iterable.  
- `StopIteration` → raised internally when the iterator ends (handled automatically).  
- Any runtime error in the loop body is propagated normally.
'''
# Example
try:
    for x in 1234:    # not iterable
        print(x)
except TypeError as e:
    print("Error:", e)



'''
Q12. Can for loops iterate over generators or files?
Ans:
Yes! For loops work with any object that follows the *iterator protocol*,  
including generators, files, and custom iterable classes.
'''
# Example
def gen():
    for i in range(3):
        yield i

for val in gen():
    print(val)  # 0 1 2

with open("sample.txt") as f:
    for line in f:
        print(line.strip())



'''
Q13. What’s the main advantage of Python’s for loop design?
Ans:
It’s *iterator-based* — meaning it works for any iterable,  
doesn’t rely on manual indexing, and automatically handles iteration end.
'''
