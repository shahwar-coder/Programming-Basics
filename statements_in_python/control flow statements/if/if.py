'''
Q1. What is the basic syntax of an if statement in Python?
Ans: 
- Syntax: if condition: block  
- The block runs only if the condition evaluates to True.  

Example:
'''
if 5 > 3:
    print("Yes")  

# Step-by-step:
# 1. Condition (5 > 3) → True
# 2. Block executes → prints "Yes"



'''
Q2. What types of values can be used in conditions?
Ans: Any value that evaluates to True/False.  
Comparisons return booleans, but other objects are also evaluated by their truthiness.
'''
# Example:
x = 10
if x == 10:
    print("x is 10")

# Step-by-step:
# 1. x == 10 → True
# 2. Block executes → prints "x is 10"



'''
Q3. What are falsy values in Python?
Ans: These evaluate to False in a boolean context:  
False, None, 0, "", [], {}, set(), range(0).

Example:
'''
if []:
    print("Non-empty")   # ❌ does not run (list is empty, falsy)



'''
Q4. What are truthy values in Python?
Ans: Any value not falsy is truthy (non-empty strings, non-zero numbers, objects).

Example:
'''
if "hello":
    print("Runs!")  

# Step-by-step:
# 1. "hello" is a non-empty string → truthy
# 2. Block executes → prints "Runs!"



'''
Q5. Why is it important to understand truthiness and falsiness?
Ans: 
- It allows writing more concise conditions.  
- Instead of checking `if len(lst) > 0:`, you can just write `if lst:`.

Example:
'''
lst = [1, 2, 3]

if lst:   # truthy since non-empty
    print("List is not empty")
