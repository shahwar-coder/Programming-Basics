'''
Q1. What is a `namedtuple`?
Ans. A `namedtuple` is a tuple where each value has a name, making the data more readable.
'''
# Example
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
# p = Point(x=3, y=4)


'''
Q2. Why are `namedtuple`s more readable than normal tuples?
Ans. Because you can access values using names instead of index numbers.
'''
# Example
# Normal tuple
pt = (3, 4)
# pt[0], pt[1]  → unclear

# namedtuple
p = Point(3, 4)
# p.x, p.y  → very clear


'''
Q3. Are `namedtuple`s mutable or immutable?
Ans. `namedtuple`s are immutable, just like normal tuples.
'''
# Example
# p.x = 10 ❌ not allowed (immutable)


'''
Q4. Why are `namedtuple`s called “immutable records”?
Ans. Because they store fixed data with named fields that cannot be changed.
'''
# Example
Student = namedtuple("Student", ["id", "name", "city"])
s = Student(101, "Rahul", "Delhi")
# Acts like a read-only record


'''
Q5. How do you access values in a `namedtuple`?
Ans. You can access values using dot notation or indexing.
'''
# Example
s.name     # "Rahul"
s[1]       # "Rahul"


'''
Q6. Why are `namedtuple`s safer than dictionaries for records?
Ans. Because field names are fixed and values cannot be accidentally changed.
'''
# Example
# Dict allows:
# record["name"] = "X" ❌ (can change anytime)
# namedtuple prevents this ✔️


'''
Q7. When should you use a `namedtuple`?
Ans. Use it for small, fixed records where readability and safety matter.
'''
# Example
# Coordinates, configs, DB rows, return values


'''
Q8. What is the one-line rule to remember?
Ans. `namedtuple` gives you readable, immutable records with named fields.
'''
# Example (lock it 🔒)
# Tuple + names + immutability = namedtuple
