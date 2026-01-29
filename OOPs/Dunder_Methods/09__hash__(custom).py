class User:
    def __init__(self, email):
        self.email = email

u1 = User("a@gmail.com")
u2 = User("a@gmail.com")

print(u1 == u2)

# False
# Python says they are different (memory-based).
# But the users are same right?

'''
Now, let's zoom in to the problem
'''

users = set()
users.add(u1)
users.add(u2)

print(len(users))

# 2 
# But since the users are actually same
# then why the deduplication did not happen ?
# Why the length is not 1 but 2 ?

'''
We will have to teach Python both are equal
'''

class User:
    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

print(u1 == u2)

# True


'''
Still not completely fixed because,
we told python what "equality" means,
we are yet to tell python, how to hash
'''
# so we see:

users = set()
users.add(u1) # TypeError: unhashable type: 'User'


'''
Now we write our hash
'''
class User:
    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)


'''
Now we can try...
'''
u1 = User("a@gmail.com")
u2 = User("a@gmail.com")

users = set()
users.add(u1)
users.add(u2)

print(len(users))

# 1
# This is expected now.


'''
Golden rule to never forget:
'''
if a == b:
    hash(a) == hash(b)


'''
# Key Points (What Problem You Hit)
- By default, Python objects are compared by identity (memory address).
- u1 == u2 is False because they are two different objects in memory.
- Even though the emails are the same, Python does NOT know your business meaning of "same".

# Why set() Did NOT Deduplicate
- set uses TWO things internally:
  1️⃣ __hash__() → to decide the bucket
  2️⃣ __eq__()   → to confirm equality inside the bucket

- Initially:
  - No __eq__ defined → identity comparison
  - No __hash__ defined → default object hash (based on memory)
- So u1 and u2:
  - Different hashes
  - Never even compared with __eq__
  → Both stay in the set → length = 2

# Partial Fix: Only __eq__
- Defining __eq__ tells Python *when* two objects are equal.
- But the moment you define __eq__, Python DISABLES __hash__ automatically.
- Reason: to prevent broken hashing logic.
- Result:
  - Object becomes unhashable
  - set.add(u1) raises TypeError

# Final Fix: __eq__ + __hash__
- __eq__ defines logical equality (same email).
- __hash__ defines how the object is placed in hash-based collections.
- Hashing the same email guarantees same hash value.

# Why hash(self.email) Works
- email is immutable (string).
- Immutable objects are safe for hashing.
- Equal emails → equal hashes → correct deduplication.

# Final Behavior
- u1 == u2 → True
- hash(u1) == hash(u2) → True
- set deduplicates correctly → length = 1

# Golden Rule (ABSOLUTELY CRITICAL)
- If a == b, then hash(a) MUST equal hash(b)
- Violating this rule breaks:
  - sets
  - dict keys
  - caches
  - lookup correctness

# Backend Mental Model
- __eq__ → business identity
- __hash__ → bucket placement
- set/dict → rely on BOTH, not just one

# Core Takeaway
- Equality alone is NOT enough for deduplication.
- Hashing alone is NOT enough either.
- For hash-based collections:
  👉 __eq__ and __hash__ must be consistent.
'''
