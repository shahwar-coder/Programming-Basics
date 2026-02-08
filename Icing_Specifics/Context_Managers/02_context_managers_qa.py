'''
Q1. What is a Context Manager in Python?
A.
A Context Manager is an object that automatically handles
setup and cleanup of a resource.
It is designed to be used with the `with` statement.
'''
# Example:
# with resource:
#     use resource
# Setup and cleanup happen automatically.


'''
Q2. Which special methods make an object a Context Manager?
A.
An object becomes a Context Manager by implementing:
- __enter__()  → setup
- __exit__()   → cleanup
'''
# Example:
# class MyCM:
#     def __enter__(self): ...
#     def __exit__(self, exc_type, exc_val, exc_tb): ...


'''
Q3. What does __enter__ do?
A.
__enter__ is called at the start of the `with` block.
It performs setup and returns the object (or a related value)
that will be used inside the block.
'''
# Example:
# def __enter__(self):
#     print("Open resource")
#     return self


'''
Q4. What does __exit__ do?
A.
__exit__ is called at the end of the `with` block.
It performs cleanup and runs even if an error occurs.
'''
# Example:
# def __exit__(self, exc_type, exc_val, exc_tb):
#     print("Close resource")


'''
Q5. What is the internal flow of a with statement?
A.
Python rewrites the with-statement to guarantee cleanup
using try/finally semantics.
'''
# Example:
# ctx = obj
# x = ctx.__enter__()
# try:
#     block
# finally:
#     ctx.__exit__(exc_type, exc_val, exc_tb)


'''
Q6. Why are Context Managers important in backend systems?
A.
Because they guarantee resource cleanup even during failures,
making systems safe and predictable.
'''
# Example:
# - Database connections always close
# - Files are always released
# - Locks never remain stuck


'''
Q7. What is the simplest mental model for a Context Manager?
A.
A Context Manager provides safe setup and guaranteed cleanup.
'''
# Example:
# with FileSim():
#     print("Reading")
# Output:
# Open
# Reading
# Close
