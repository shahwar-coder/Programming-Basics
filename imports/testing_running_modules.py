'''
Q1. What does the __name__ variable mean in Python?
Ans:
- When a file is imported, __name__ = "modulename".
- When a file is run directly, __name__ = "__main__".
'''
# Example: file demo.py
print("__name__ is", __name__)

# Running: python demo.py
# → __name__ is __main__

# Importing: import demo
# → __name__ is demo



'''
Q2. Why use if __name__ == "__main__" ?
Ans:
- Without it: top-level code runs on import, which is often unintended.
- With it: top-level code runs only when file is executed directly, 
  not when imported → safer, reusable modules.
'''
# utils.py
def add(x, y): 
    return x + y

print(add(2, 3))   # top-level code, always runs

'''
❌ Problem: No main guard:
$ python utils.py
5   # ✅ works when run directly

$ python
>>> import utils
5   # ❌ runs again (unwanted side effect!)
'''

'''
✅ Fix: Use main guard:
# utils.py
def add(x, y): 
    return x + y

if __name__ == "__main__":   # guard
    print(add(2, 3))

======

$ python utils.py
5   # ✅ prints only when run directly

$ python
>>> import utils
# (nothing printed) ✅ safe import
'''
'''
Conclusion:
Step-by-step:
1. When run directly: __name__ == "__main__" → guard passes → code executes.
2. When imported: __name__ == "utils" → guard fails → code skipped.
'''



'''
Q3. What is python -m and why is it useful?
Ans:
- Runs a module in its package context.
- Fixes relative import issues compared to running file directly.

Example:
python -m mypkg.main

# vs python mypkg/main.py
# → the -m version treats mypkg as a proper package,
# avoiding ImportError for relative imports.
'''



'''
Q4. What are common uses of __main__ guard?
Ans:
- For demo/testing code inside a module.
- For command-line scripts (entry points).
- For package-safe execution (with python -m).

Example:
'''
def main():
    print("Program running")

if __name__ == "__main__":
    main()
