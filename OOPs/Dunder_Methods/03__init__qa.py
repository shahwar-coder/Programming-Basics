'''
Q1. What is the purpose of the __init__ method in Python?
A.
__init__ is used to initialize an object after it has been created.
Its job is to set up the object’s attributes so the object is ready to use.
'''
# Example:
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# u = User(1, "Rahul")


'''
Q2. Does __init__ create the object in memory?
A.
No. __init__ does NOT create the object.
The object is already created before __init__ runs.
__init__ only fills the object with data.
'''
# Example:
# u = User(1, "Rahul")
# Step 1: Python creates an empty User object
# Step 2: __init__ assigns id and name


'''
Q3. When is __init__ automatically called?
A.
__init__ is called automatically immediately after an object
is instantiated using the class name.
'''
# Example:
# u1 = User(1, "Rahul")   # __init__ runs here
# u2 = User(2, "Joel")   # __init__ runs again for this object


'''
Q4. What is the main responsibility of __init__?
A.
The main responsibility of __init__ is to initialize
the object’s state by assigning attributes.
'''
# Example:
# class User:
#     def __init__(self, email):
#         self.email = email


'''
Q5. Can __init__ be used for validation?
A.
Yes. __init__ is commonly used to validate input
before storing it on the object.
'''
# Example:
# class User:
#     def __init__(self, email: str):
#         if "@" not in email:
#             raise ValueError("Invalid email")
#         self.email = email.lower()


'''
Q6. What happens if validation in __init__ fails?
A.
If validation fails, object creation stops and an exception is raised.
The object is never fully initialized.
'''
# Example:
# User("invalid-email")  # raises ValueError
