'''
Context Manager — extremely concise, effective summary

What is a Context Manager (CM)?
- An object that handles setup and cleanup automatically.
- Used with the `with` statement.

Core idea:
- __enter__ → setup (start using resource)
- __exit__ → cleanup (release resource)

Why it matters:
- Ensures cleanup happens even if an error occurs.

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

Simple example:

class FileSim:
    def __enter__(self):
        print("Open")
        return self
    def __exit__(self, *args):
        print("Close")

with FileSim():
    print("Reading")

Output:
Open
Reading
Close

One-line idea:
Context Manager = safe setup + guaranteed cleanup.
'''
