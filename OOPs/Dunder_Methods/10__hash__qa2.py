'''
Q1. Why does `u1 == u2` return False by default for custom objects?
A.
Because Python compares custom objects by identity (memory address) by default.
Even if their attributes are the same, Python treats them as different objects
unless you explicitly define equality logic.
'''
# Example:
# class User:
#     def __init__(self, email):
#         self.email = email
#
# User("a@gmail.com") == User("a@gmail.com")
# Output: False


'''
Q2. Why did `set()` not deduplicate u1 and u2?
A.
Because sets rely on hashing and equality.
Without custom __eq__ and __hash__, Python places objects into
different hash buckets and never considers them equal.
'''
# Example:
# users = set()
# users.add(u1)
# users.add(u2)
# len(users)
# Output: 2


'''
Q3. What problem does defining only __eq__ solve?
A.
Defining __eq__ teaches Python what "logical equality" means
based on business rules (like same email).
But it does NOT make the object usable in sets or dicts.
'''
# Example:
# def __eq__(self, other):
#     return self.email == other.email
#
# u1 == u2
# Output: True


'''
Q4. Why does defining __eq__ make the object unhashable?
A.
When __eq__ is defined, Python disables __hash__ automatically
to prevent inconsistent hashing behavior that could corrupt sets or dicts.
'''
# Example:
# users.add(u1)
# TypeError: unhashable type: 'User'


'''
Q5. Why is __hash__ required for sets and dict keys?
A.
Because hash-based collections use hash values to decide
where objects live internally (buckets).
Without a hash, Python cannot store the object safely.
'''
# Example:
# def __hash__(self):
#     return hash(self.email)


'''
Q6. What is the golden rule linking __eq__ and __hash__?
A.
If two objects are equal according to __eq__,
they MUST return the same hash value.
Breaking this rule breaks sets, dicts, caches, and lookups.
'''
# Example:
# if a == b:
#     hash(a) == hash(b)
