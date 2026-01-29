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

