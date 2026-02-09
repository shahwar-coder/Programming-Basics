'''
Q1. What are dunder (double-underscore) methods in Python?
A.
Dunder methods are special methods that define how an object behaves
when Python itself interacts with it.
They act as contracts between your class and the Python runtime.
'''
# Example:
# __init__  → object creation
# __repr__  → printing in logs/debuggers
# __eq__    → equality checks
# __iter__  → looping
# __enter__ → with-statement support


'''
Q2. What is the purpose of __init__?
A.
__init__ initializes the object’s valid state immediately after creation.
It sets attributes and enforces invariants, but should NOT perform heavy work.
'''
# Example:
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
# User(1, "Rahul")  # __init__ runs automatically


'''
Q3. What is the difference between __repr__ and __str__?
A.
__repr__ is for developers (logs, debugging, tracing).
__str__ is for users (friendly display).
If __str__ is missing, Python falls back to __repr__.
'''
# Example:
# print(obj)        → __str__
# repr(obj)         → __repr__
# logs/debuggers    → __repr__


'''
Q4. Why is __eq__ considered business logic?
A.
Because equality for objects should reflect business identity,
not memory location.
Two different objects can represent the same real-world entity.
'''
# Example:
# User(id=1, email="a@mail.com") == User(id=1, email="b@mail.com")
# True  # same business identity (id)


'''
Q5. Why must __eq__ and __hash__ be implemented together?
A.
Because hash-based collections (set, dict) rely on BOTH.
If two objects are equal, they MUST have the same hash.
'''
# Example:
# if a == b:
#     hash(a) == hash(b)
# Required for correct behavior in sets, dict keys, caches


'''
Q6. What does __bool__ control?
A.
__bool__ defines how an object behaves in truth-value checks.
It answers the question: “Is this object true or false?”
'''
# Example:
# class FeatureFlag:
#     def __bool__(self):
#         return self.enabled
# if feature_flag:
#     enable_feature()


'''
Q7. What role do __len__ and __iter__ play?
A.
__len__ defines size semantics.
__iter__ defines how an object is traversed in loops.
Together, they make objects behave like collections.
'''
# Example:
# len(cart)        → __len__
# for item in cart → __iter__


'''
Q8. Why are __enter__ and __exit__ critical for backend systems?
A.
They enable context managers, guaranteeing setup and cleanup
even when errors occur.
This is essential for resource safety.
'''
# Example:
# with DBSession():
#     run_queries()
# Connection is always closed


'''
Q9. What does __getitem__ enable?
A.
__getitem__ allows objects to support index or key access using [].
It makes objects behave like dictionaries or lists.
'''
# Example:
# config["db_host"] → __getitem__


'''
Q10. What is the purpose of __call__?
A.
__call__ makes an object callable like a function.
It’s commonly used for validators, strategies, and policies.
'''
# Example:
# validator = Validator()
# validator(value)  # calls __call__


'''
Q11. How do dataclasses relate to dunder methods?
A.
Dataclasses automatically generate common dunder methods
like __init__, __repr__, and __eq__ to reduce boilerplate.
'''
# Example:
# @dataclass
# class User:
#     id: int
#     name: str
# __init__, __repr__, __eq__ are auto-created


'''
Q12. What is the correct mental model for dunder methods?
A.
Dunder methods define how your objects behave when Python interacts with them.
They bridge your domain logic with Python’s runtime behavior.
'''
# Example:
# Object + dunder methods = Python-native behavior
