'''
Q1. What is __repr__ in Python?
A.
__repr__ is a special method that defines how an object is represented
as a string for developers.
It is mainly used for debugging, logging, and inspection.
'''
# Example:
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def __repr__(self):
#         return f"User(id={self.id}, name={self.name})"
#
# print(User(1, "Rahul"))
# Output: User(id=1, name=Rahul)


'''
Q2. When is __repr__ automatically used?
A.
__repr__ is used when:
- an object is printed
- an object appears in logs
- an object is inspected in a debugger
- an object appears inside a list or dict
'''
# Example:
# users = [User(1, "Rahul"), User(2, "Joel")]
# print(users)
# Output: [User(id=1, name=Rahul), User(id=2, name=Joel)]


'''
Q3. Why is __repr__ important for backend engineers?
A.
Backend engineers rely on __repr__ for:
- readable logs
- clear debugging output
- useful error traces
- observability in production systems
'''
# Example:
# logger.info(user)
# Good __repr__ makes logs meaningful
# Bad __repr__ makes logs useless


'''
Q4. What is the golden rule for writing __repr__?
A.
__repr__ should be:
- unambiguous (clearly identify the object)
- short (easy to scan)
- safe (must not expose secrets)
'''
# Example:
# return f"User(id={self.id}, name={self.name})"  # GOOD


'''
Q5. What should NEVER be included in __repr__?
A.
Sensitive or secret data should never appear in __repr__.
This includes passwords, tokens, API keys, or secrets.
'''
# Example (BAD):
# return f"User(password={self.password})"
#
# Why bad:
# - leaks secrets into logs
# - security risk
# - production incidents waiting to happen


'''
Q6. What happens if __repr__ is not defined?
A.
Python uses a default representation that is not helpful,
usually showing only the memory address.
'''
# Example:
# class User:
#     pass
#
# print(User())
# Output: <__main__.User object at 0x10af3c820>
