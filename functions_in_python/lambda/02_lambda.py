'''
Q1. Why are lambda functions useful in Python?
Ans:
Lambda functions are great for **small, one-time operations** —  
when defining a full `def` function would be unnecessary.  
They are often used as **inline helpers** or quick callbacks.
'''
# Example
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]


'''
Q2. How can lambda functions be returned from other functions?
Ans:
A normal function can **return** a lambda, creating a small “function factory.”  
This is common in functional programming patterns.
'''
# Example
def myfunc(n):
    return lambda a: a * n

doubler = myfunc(2)
print(doubler(10))  # 20


'''
Q3. What happens when you call `myfunc(3)` in the above example?
Ans:
`myfunc(3)` returns a lambda that multiplies any input by **3**.  
It remembers the value `n=3` through a **closure**.
'''
# Example
tripler = myfunc(3)
print(tripler(5))  # 15


'''
Q4. What is a closure and how does lambda use it?
Ans:
A **closure** is when an inner function (like a lambda)  
remembers variables from the outer function’s scope even after it has finished running.
'''
# Example
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(4), triple(4))  # 8 12


'''
Q5. When should you prefer lambda functions over def?
Ans:
✅ Use `lambda` when:
- Function logic fits in one simple expression  
- It’s used only once or passed as a quick argument  

❌ Use `def` when:
- You need multiple lines or statements  
- You want better readability or reuse
'''
# Example
# ✅ Perfect for one-liner use
print(sorted(["apple", "Banana", "cherry"], key=lambda x: x.lower()))
# The sorted() function can take a key argument to customize sorting.
# Here, key=lambda x: x.lower converts each string to lowercase before comparison.
# This ensures case-insensitive sorting without altering the actual data.
# So, sorted(["apple", "Banana", "cherry"], key=lambda x: x.lower)
# → ['apple', 'Banana', 'cherry']


'''
Q6. What is the benefit of using lambdas as function arguments?
Ans:
They let you pass **custom logic** without defining a named function.
'''
# Example
nums = [5, 1, 3, 9]
print(sorted(nums, key=lambda x: -x))  # [9, 5, 3, 1]
# • sorted() normally sorts in ascending order.
# • key=lambda x: -x → negates each number before comparison.
# • Negative values reverse the order effectively.
# • Result: sorts in descending order → [9, 5, 3, 1]


'''
Q7. Can lambda functions access variables defined outside them?
Ans:
Yes — lambdas **capture** variables from the outer scope (like closures).  
However, they can’t reassign them directly.
'''
# Example
factor = 10
scale = lambda x: x * factor
print(scale(3))  # 30


'''
Q8. Can you have multiple lambda “instances” from one outer function?
Ans:
Yes — each returned lambda keeps its **own captured variable** from the outer call.
'''
# Example
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))  # 10 15
 

'''
Q9. Are lambda functions faster than regular functions?
Ans:
Not significantly — they’re mostly about **convenience and readability**,  
not performance. Both compile to similar bytecode.
'''
# (No specific example required)


'''
Q10. Summary:
Ans:
✅ When to Use Lambdas  
- Short, throwaway functions  
- Passing logic to `map()`, `filter()`, `sorted()`  
- Returning custom one-liners from other functions  
- Functional patterns (closures, callbacks)

✅ Key Concept:  
Lambdas + closures = flexible, compact, and powerful inline logic.
'''
