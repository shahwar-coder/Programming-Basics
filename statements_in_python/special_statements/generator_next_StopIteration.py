'''
📌 Understanding Generators, next(), and StopIteration

1. Generator basics
• A function with `yield` → generator function
• Calling it returns a generator object (not values immediately)
• Use `next()` to step through values one by one

2. Example
def g():
    yield 1
    return 5

gen = g()
print(next(gen))   # 1 → pauses at yield
print(next(gen))   # raises StopIteration(5)

3. What happens
• First next() → yields 1, pauses
• Second next() → hits return, generator ends
  → raises StopIteration with value 5

4. Why StopIteration matters
• for-loops handle StopIteration automatically (so you don’t see it)
• The return value (5) is hidden unless:
   – You manually catch StopIteration
   – Or you use "yield from" in another generator

✅ Summary
• Generators produce values one at a time with yield
• When finished, they raise StopIteration
• return value in a generator is stored in StopIteration.value
'''


'''
Some Questions:
'''


'''
Q1. What happens when you call a generator function?
Ans: It doesn’t run immediately. Instead, it returns a generator object, 
which can be iterated with next() or in a for-loop.

Example:
'''

def g():
    yield 1
gen = g()
print(gen)   # <generator object g at ...>



'''
Q2. How does next() work on a generator?
Ans: next() runs the generator until the next yield.  
- If yield is reached → returns the value and pauses.  
- If return is reached → raises StopIteration (with optional value).
'''
def g(): 
    yield 10
gen = g()
print(next(gen))   # 10
# next(gen) → StopIteration



'''
Q3. What happens when a generator hits a return statement?
Ans: It raises StopIteration.  
- If the return has a value → that value is stored in StopIteration.value.  
- If no value → StopIteration(None).
'''
def g(): 
    return 99
gen = g()
try:
    next(gen)
except StopIteration as e:
    print("StopIteration value:", e.value)   # 99



'''
Q4. Why don’t you usually see StopIteration when looping over a generator?
Ans: Because for-loops and other iteration contexts 
catch StopIteration automatically to end the loop cleanly.
'''
def g():
    yield 1
    yield 2
for val in g():
    print(val)   # 1, 2
# Loop ends silently when StopIteration is raised.

'''
Q5. (Coding)
# Predict the outputs

def g():
    yield "first"
    return "done"

gen = g()
print("Step 1:", next(gen))

try:
    print("Step 2:", next(gen))
except StopIteration as e:
    print("Generator stopped with:", e.value)
'''

def g():
    yield "first"
    return "done"

gen = g()
print("Step 1:", next(gen))

try:
    print("Step 2:", next(gen))
except StopIteration as e:
    print("Generator stopped with:", e.value)


'''
Actual Output:
Step 1: first
Generator stopped with: done
'''

'''
Explanation:
- First next(gen) → runs until yield "first". 
  Returns "first", so prints: Step 1: first.

- Second next(gen) → reaches return "done".
  That raises StopIteration("done").
  The print("Step 2:", ...) never runs, 
  because the exception interrupts before it can execute.

- The except block catches StopIteration and prints 
  its .value → "done".

- If not caught, Python would show a traceback ending with StopIteration: done.
- In a for-loop, StopIteration is swallowed silently → loop ends.
'''


