'''
__str__ : Defines what your object shows when you print the object
'''

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Harry Potter")
print(b)

# Output
# Book: Harry Potter
