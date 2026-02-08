'''
Things like :

with open("file.txt") as f:
    data = f.read()

work because, file object has these two methods to help Python `setup` and `cleanup` automatically.
'''

'''
__enter__, __exit__ and Context Manager — ultra-concise summary

What is a Context Manager (CM)?
- A context manager is an object that controls setup and cleanup of a resource.
- It works with the `with` statement.
- It must define: __enter__ and __exit__.

Why __enter__ and __exit__?
- They are the methods that make an object a context manager.
- __enter__ → runs at the start (setup)
- __exit__ → runs at the end (cleanup), even if an error occurs

Internal flow:
with obj as x:
    block

Python does:
ctx = obj
x = ctx.__enter__()
try:
    block
finally:
    ctx.__exit__(exc_type, exc_val, exc_tb)

Key idea:
- Context Manager = object that safely handles resources
- __enter__ = start using resource
- __exit__ = release/clean the resource

Simple example:

class FileSim:
    def __enter__(self):
        print("Open file")
        return self
    def __exit__(self, *args):
        print("Close file")

with FileSim():
    print("Reading")

Output:
Open file
Reading
Close file
'''


class FakeFile:
    def __enter__(self):
        print("Opening file")
        return self

    def read(self):
        return "Some data"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file")

with FakeFile() as f:
    print(f.read())

# Opening file
# Some data
# Closing file

