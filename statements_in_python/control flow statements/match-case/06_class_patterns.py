'''
Q1. What are class patterns in Python’s match/case?
Ans:
Class patterns let you match objects by their class type and attributes,  
and extract those attribute values directly into variables.
'''
# Example
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(0, 5)

match p:
    case Point(x=0, y=y_val):
        print(f"On Y-axis at {y_val}")   # On Y-axis at 5



'''
Q2. What’s the syntax for matching a class pattern?
Ans:
Use the class name followed by attributes in parentheses:  
`case ClassName(attr1=value1, attr2=var):`
'''
# Example
match p:
    case Point(x=1, y=y_val):
        print("At x=1, y=", y_val)



'''
Q3. What’s the key takeaway of class pattern matching?
Ans:
It’s like doing `isinstance()` + attribute unpacking + comparison  
all in one step — concise, powerful, and Pythonic for object-based data.
'''
# Example
@dataclass
class Circle:
    radius: int

shape = Circle(10)
match shape:
    case Circle(radius=r):
        print("Circle radius =", r)
      
# Enter match with value shape = Circle(10).
# Evaluate the first case: Circle(radius=r).
# Type check: Python asks isinstance(shape, Circle) → True.
# Attribute access: Python retrieves shape.radius (value 10)
# Binding: Bind the attribute value to name r → r = 10.
# Enter the case block because the pattern succeeded.
# Execute print("Circle radius =", r) → prints Circle radius = 10.
# Exit the match (no further cases are tried).
