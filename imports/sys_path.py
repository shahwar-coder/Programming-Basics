'''
Q1. What is sys.path in Python?
Ans: A list of directories Python searches in order to find modules for import.

Example:
'''
import sys
print(sys.path[:3])   # shows first few search paths



'''
Q2. What is the module search order?
Ans:
1. Current directory / script directory
2. PYTHONPATH (if set)
3. Standard library directories
4. site-packages (third-party packages)

Example:
# If you have a file named math.py in current dir,
# `import math` will load that instead of stdlib math.
'''



'''
Q3. What happens when multiple modules with the same name exist in sys.path?
Ans: Python stops at the first match.  
This means a local file can shadow a standard library module.

Example:
If you have a file named random.py locally, 
`import random` will import your file instead of stdlib random.
'''



'''
Q4. How can sys.path be modified?
Ans:
- At runtime: sys.path.append("dir")
- Using PYTHONPATH environment variable
Best practice: avoid modifying sys.path directly; use packages instead.
'''



'''
Q5. Coding output ? 
'''
import sys

print("Type of sys.path:", type(sys.path))
print("First entry in sys.path:", sys.path[0])

sys.path.append("my_extra_dir")
print("Last entry in sys.path:", sys.path[-1])

'''
Actual Output:
Type of sys.path: <class 'list'>
First entry in sys.path: ''      # empty string = current directory
Last entry in sys.path: my_extra_dir
'''

'''
Explanation:
- sys.path is always a list → so its type prints as <class 'list'>, not <String>.
- sys.path[0] is usually an empty string '' when running an interactive session, 
  meaning "current working directory". 
  (When running a script, it may be the script’s directory instead.)
- After sys.path.append("my_extra_dir"), the last entry becomes "my_extra_dir".
'''
