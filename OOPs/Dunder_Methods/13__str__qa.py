'''
Q1. What is __str__ in Python?
A.
__str__ is a special method that defines how an object describes itself
when it is printed using print().
It must always return a string.
'''
# Example:
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"My name is {self.name}"
#
# print(Dog("Buddy"))
# Output: My name is Buddy


'''
Q2. What happens if __str__ is NOT defined?
A.
Python falls back to a default representation that shows
the class name and memory address, which is not human-friendly.
'''
# Example:
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
# print(Dog("Buddy"))
# Output: <__main__.Dog object at 0x10ab3f>


'''
Q3. When exactly is __str__ called?
A.
__str__ is called whenever Python needs a human-readable
string version of the object, especially with print().
'''
# Example:
# d = Dog("Buddy")
# print(d)        # calls d.__str__()
# str(d)          # also calls d.__str__()


'''
Q4. What is the purpose of __str__?
A.
Its purpose is readability for humans:
logs, console output, debugging, and simple display.
'''
# Example:
# class Book:
#     def __init__(self, title):
#         self.title = title
#     def __str__(self):
#         return f"Book: {self.title}"
#
# print(Book("Harry Potter"))
# Output: Book: Harry Potter


'''
Q5. What are the rules for __str__?
A.
- It must return a string
- It should be simple and readable
- It should not expose sensitive data
'''
# Example:
# GOOD:  "User(id=1, name=Rahul)"
# BAD:   "User(password=secret123)"


'''
Q6. How should you mentally think about __str__?
A.
Think of __str__ as:
"How should this object introduce itself to a human?"
'''
# Example:
# Dog → "My name is Buddy"
# Car → "Red Toyota car"
# Book → "Book: Harry Potter"
