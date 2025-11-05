'''
Q1. What does “binding variables” mean in match/case?
Ans:
It means capturing parts of a matched value into variables,  
so you can use those parts directly in your code.
'''
value = 42
match value:
    case x:
        print("Inside case: x =", x)
# match looks at value (which is 42).
# case x: is a name pattern — it matches any value and binds that value to the name x.
# Because it matched, x is assigned 42, and print prints x = 42.

point = (3, 4)
match point:
    case (x, y):
        print("x =", x, "y =", y)
# match inspects point, a 2-tuple (3, 4).
# Pattern (x, y) requires a 2-element sequence and says: bind first element to x, second to y.
# Since point fits, x = 3 and y = 4 after the match; they can be used inside the block.

data = [1, 2, 3, 4]
match data:
    case [first, *rest]:
        print("first =", first)
        print("rest =", rest)
# match checks data.
# Pattern [first, *rest] matches any sequence with at least one element, binds head to first and the remaining elements to rest (a list).
# For [1,2,3,4], first = 1, rest = [2,3,4].

value = ("user", ("alice", 30))
match value:
    case ("user", (name, age)):
        print(f"{name=} {age=}")
# Nested Pattern
# match sees a nested tuple structure.
# The pattern requires an outer tuple ("user", inner) and then destructures inner into name and age.
# If structure and literal "user" match, name = "alice", age = 30.

record = [10, 20, 30]
match record:
    case [first, *rest] as whole:
        print("first:", first)
        print("rest:", rest)
        print("whole:", whole)
# Binding parts, rest and whole
# Pattern [first, *rest] as whole first checks the structural match.
# If it matches, it binds first and rest as usual and also binds the entire matched value to whole.
# Result: first = 10, rest = [20,30], whole = [10,20,30].

payload = {"type": "login", "user": "bob"}
match payload:
    case {"type": t, "user": u}:
        print(t, u)
# Dict-Style
# The mapping pattern checks keys "type" and "user" exist in the dict.
# If they do, it binds their corresponding values to t and u.
# Here t = "login", u = "bob".



'''
Q2. How does simple variable capture work?
Ans:
If you use just a variable name in a case (like `case x:`),  
it always matches and binds the *entire* value to that variable.
'''
# Example
name = "Alice"
match name:
    case person:
        print("Matched name:", person)



'''
Q3. What are positional patterns in match/case?
Ans:
They let you unpack sequences like tuples or lists directly.  
Variables in the pattern receive values from matching positions.
'''
# Example
match (10, 20):
    case (x, y):
        print("x =", x, "y =", y)   # 10 20



'''
Q4. How does the *rest syntax work in list patterns?
Ans:
You can use `*rest` to capture remaining items of a list.  
It works like unpacking in normal Python assignments.
'''
# Example
match [1, 2, 3, 4]:
    case [first, *rest]:
        print(first, rest)   # 1 [2, 3, 4]



'''
Q5. Can we bind attributes from class objects too?
Ans:
Yes! Use keyword or attribute patterns.  
You can match fields by name and capture them into variables.
'''
# Example
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

p = Point(1, 9)

match p:
    case Point(x=1, y=y_val):
        print("y =", y_val)   # binds y_val = 9



'''
Q6. What are the main benefits of binding in patterns?
Ans:
- Combines matching and unpacking in one step.  
- Cleaner and more readable than nested unpacking.  
- Great for tuples, lists, and dataclasses.
'''



'''
Q7. What’s the key idea behind binding patterns?
Ans:
Patterns can both *test structure* (does it fit?)  
and *assign parts* (store pieces into variables)  
at the same time — making code concise and expressive.
'''
