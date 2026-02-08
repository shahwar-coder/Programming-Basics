'''
Q1. Why does the `with` statement exist in Python?
A.
The `with` statement exists to manage resources safely.
It guarantees that setup happens before use and cleanup happens after use,
even if an error occurs.
'''
# Example:
# with open("file.txt") as f:
#     data = f.read()
# File is ALWAYS closed automatically.


'''
Q2. What is a Context Manager?
A.
A context manager is an object that controls:
- setup of a resource
- cleanup of a resource
using the `with` statement.
'''
# Example:
# File objects, database connections, locks
# are all context managers.


'''
Q3. Which methods make an object a Context Manager?
A.
An object becomes a context manager if it defines:
- __enter__()
- __exit__()
'''
# Example:
# __enter__ → setup
# __exit__  → cleanup


'''
Q4. What does __enter__ do?
A.
__enter__ runs at the START of the `with` block.
It prepares the resource and returns the object
that will be assigned after `as`.
'''
# Example:
# def __enter__(self):
#     print("Opening file")
#     return self


'''
Q5. What does __exit__ do?
A.
__exit__ runs at the END of the `with` block.
It cleans up the resource and runs EVEN IF an exception occurs.
'''
# Example:
# def __exit__(self, exc_type, exc_val, exc_tb):
#     print("Closing file")


'''
Q6. What is the exact internal flow of `with`?
A.
Python rewrites:
with obj as x:
    block

into:
'''
# Example:
# ctx = obj
# x = ctx.__enter__()
# try:
#     block
# finally:
#     ctx.__exit__(exc_type, exc_val, exc_tb)


'''
Q7. Why is __exit__ given exception details?
A.
So the context manager can:
- clean up safely
- optionally suppress exceptions
'''
# Example:
# def __exit__(self, exc_type, exc_val, exc_tb):
#     if exc_type:
#         log_error(exc_val)
#     return False   # re-raise exception


'''
Q8. What problem do Context Managers solve in real systems?
A.
They prevent resource leaks.
No matter what happens inside the block,
cleanup is GUARANTEED.
'''
# Example:
# - files always close
# - DB connections always release
# - locks always unlock


'''
Q9. Why is `with open(...)` so important?
A.
Because files are OS-level resources.
Forgetting to close them causes:
- memory leaks
- file locks
- production bugs
'''
# Example:
# with open("data.txt") as f:
#     process(f)
# No manual close() needed.


'''
Q10. Core mental model (memorize)
A.
Context Manager =
"I will take responsibility for setup and cleanup."
'''
# Example:
# __enter__ → start using resource
# __exit__  → stop using resource safely
