'''
Q1. What is __eq__ in Python?
A.
__eq__ is a special method that defines how the == operator works
for objects of a class.
It decides when two objects should be considered equal.
'''
# Example:
# class User:
#     def __init__(self, id, email):
#         self.id = id
#         self.email = email
#
#     def __eq__(self, other):
#         return self.id == other.id
#
# User(1, "a@mail.com") == User(1, "b@mail.com")
# Output: True


'''
Q2. What does Python do if __eq__ is NOT defined?
A.
If __eq__ is not defined, Python falls back to default behavior,
which usually compares object identity (memory location),
not the actual data inside the objects.
'''
# Example:
# class User:
#     def __init__(self, id):
#         self.id = id
#
# User(1) == User(1)
# Output: False (different objects in memory)


'''
Q3. Why is __eq__ considered business logic in backend systems?
A.
Because equality depends on domain rules, not memory.
Two objects may represent the same real-world entity
even if they are different instances.
'''
# Example:
# Users compared by id (business identity)
# Orders compared by order_id
# Accounts compared by email or username


'''
Q4. Why should isinstance(other, ClassName) be checked in __eq__?
A.
To ensure comparison only happens between compatible types.
If types don’t match, returning NotImplemented allows Python
to handle comparison safely.
'''
# Example:
# def __eq__(self, other):
#     if not isinstance(other, User):
#         return NotImplemented
#     return self.id == other.id


'''
Q5. How do primitive types compare equality?
A.
Primitive types like int, str, and float compare by value by default.
Custom objects do NOT do this unless __eq__ is implemented.
'''
# Example:
# 5 == 5            # True
# "hi" == "hi"      # True
#
# class A: pass
# A() == A()        # False


'''
Q6. What critical rule must you remember when implementing __eq__?
A.
If you implement __eq__, you must think about hashing (__hash__).
Objects used as dictionary keys or set members must remain hash-consistent.
'''
# Example:
# If two objects are equal (a == b),
# then their hash values must also be equal.
