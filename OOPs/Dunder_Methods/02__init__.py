'''
- __init__ runs automatically right after an object is created
- It does NOT create the object itself
- By the time __init__ runs, the object already exists in memory
- Its responsibility is to initialize the object's state (attributes)
- In short: __init__ sets up the object so it’s ready to use
'''

class User:
  def __init__(self, id, name):
    self.id = id
    self.name = name

u1 = User(1, "Rahul")
u2 = User(2, "Joel")

# What Happens is:
'''
Python creates an empty object
__init__ fills it with data
'''

# __init__ can also be used to validate intervals

class User:
  def __init__(self, email: str):
    if "@" not in email:
      raise ValueError("Invalid Email")
    self.email = email.lower()
