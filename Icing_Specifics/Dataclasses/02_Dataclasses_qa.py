'''
Q1. What problem do dataclasses solve in Python?
A.
Dataclasses solve the problem of writing repetitive boilerplate code
for classes whose main purpose is to store data.
They automatically generate __init__, __repr__, and __eq__ methods.
'''
# Example:
# from dataclasses import dataclass
#
# @dataclass
# class User:
#     id: int
#     name: str
#     email: str
#
# u = User(1, "Rahul", "rahul@mail.com")
# print(u)


'''
Q2. Why are dataclasses popular in backend development?
A.
Backend engineers use dataclasses because they provide clean,
typed, readable data containers that are easy to log, debug,
and convert to dictionaries or JSON.
'''
# Example:
# user = User(1, "Rahul", "rahul@mail.com")
# asdict(user) → {'id': 1, 'name': 'Rahul', 'email': 'rahul@mail.com'}


'''
Q3. How do default values and Optional fields work in dataclasses?
A.
Dataclasses allow default values and Optional fields to represent
data that may or may not be present, without requiring extra logic.
'''
# Example:
# @dataclass
# class Product:
#     id: int
#     name: str
#     price: float
#     description: Optional[str] = None
#
# Product(1, "Laptop", 75000.0)


'''
Q4. Why should mutable defaults be avoided in dataclasses?
A.
Using mutable defaults like lists can cause shared state bugs
across instances. default_factory ensures a new object per instance.
'''
# Example:
# @dataclass
# class Order:
#     items: list = field(default_factory=list)


'''
Q5. What does frozen=True do in a dataclass?
A.
frozen=True makes the dataclass immutable.
Once created, its fields cannot be modified.
'''
# Example:
# @dataclass(frozen=True)
# class Token:
#     value: str
#
# token.value = "x"  # ❌ error


'''
Q6. What is __post_init__ used for in dataclasses?
A.
__post_init__ allows adding custom logic or validation
after the auto-generated __init__ runs.
'''
# Example:
# @dataclass
# class Employee:
#     salary: float
#
#     def __post_init__(self):
#         if self.salary < 0:
#             raise ValueError("Invalid salary")
