'''
Q1. What is the difference between __str__ and __repr__?
A.
__str__ is for humans (readable, friendly output).
__repr__ is for developers (precise, unambiguous, debugging-friendly).

Rule of thumb:
- print(object) → __str__
- debugging / logs / console → __repr__
'''
# Example:
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#     def __str__(self):
#         return f"{self.name}"
#     def __repr__(self):
#         return f"User(id={self.id}, name={self.name})"
#
# u = User(1, "Rahul")
# print(u)        → Rahul
# u               → User(id=1, name=Rahul)


'''
Q2. What happens if __str__ is NOT defined but __repr__ is?
A.
Python falls back to __repr__ when __str__ is missing.
So __repr__ becomes the default printed representation.
'''
# Example:
# class Item:
#     def __repr__(self):
#         return "Item(repr)"
#
# print(Item())
# Output: Item(repr)


'''
Q3. Why do backend engineers care more about __repr__ than __str__?
A.
Because __repr__ appears in:
- logs
- stack traces
- debuggers
- interactive shells

Bad __repr__ makes debugging painful.
'''
# Example:
# ❌ Bad repr:
# <User object at 0x1093a8>
#
# ✅ Good repr:
# User(id=42, email='a@gmail.com')


'''
Q4. How do dataclasses handle __str__ and __repr__ by default?
A.
dataclasses AUTO-GENERATE both __str__ and __repr__,
and they are usually IDENTICAL and developer-friendly.
'''
# Example:
# from dataclasses import dataclass
#
# @dataclass
# class User:
#     id: int
#     name: str
#
# u = User(1, "Rahul")
# print(u)
# User(id=1, name='Rahul')
#
# u
# User(id=1, name='Rahul')


'''
Q5. How does Pydantic handle __str__ and __repr__?
A.
Pydantic focuses on:
- structured output
- JSON-like readability
- API friendliness

__repr__ is detailed and explicit.
__str__ is clean but still informative.
'''
# Example:
# from pydantic import BaseModel
#
# class User(BaseModel):
#     id: int
#     email: str
#
# u = User(id=1, email="a@gmail.com")
# print(u)
# id=1 email='a@gmail.com'
#
# u
# User(id=1, email='a@gmail.com')


'''
Q6. Why is relying on __str__ dangerous in APIs?
A.
Because __str__ is meant for HUMANS, not MACHINES.
APIs should return structured data (JSON), not stringified objects.
'''
# Example:
# ❌ BAD API RESPONSE:
# return str(user)
#
# ✅ GOOD API RESPONSE:
# return user.dict()   # Pydantic
# return asdict(user) # dataclass


'''
Q7. When should you override __str__ or __repr__ yourself?
A.
Override __repr__ when:
- debugging clarity matters
- objects appear in logs
- identity must be explicit

Override __str__ when:
- objects are printed for users
- CLI tools
- admin scripts
'''
# Example:
# __repr__ → backend / logs
# __str__  → CLI / human output


'''
Q8. Golden backend rule (memorize this)
A.
- __repr__ answers: "What exactly is this object?"
- __str__ answers:  "How should this look to a human?"
'''
# Example:
# repr(User) → precise
# str(User)  → friendly
