'''
Q1. What is the difference between a module and a package?
Ans:
- Module = single .py file.
- Package = directory with __init__.py (may contain modules/subpackages).

Example:
# mymodule.py → import mymodule
# mypkg/__init__.py, mypkg/utils.py → import mypkg.utils
'''



'''
Q2. What is a namespace package, and how is it different from a normal package?
Ans:
- Namespace package = package without __init__.py.
- Can span multiple directories on sys.path.
- Normal package = has __init__.py, lives in one directory.

Example:
mypkg/ (no __init__.py)
   sub1/
   sub2/
import mypkg.sub1, mypkg.sub2
'''



'''
Q3. What happens when you import a package with __init__.py?
Ans: Python runs the code in __init__.py once. 
You can use it to initialize state, expose submodules, or control exports.

Example:
# mypkg/__init__.py
print("mypkg imported")
'''



'''
Q4. Why are namespace packages useful?
Ans:
- Large/distributed projects (different teams own different parts).
- Multiple directories can contribute to the same package name.
- Used in big frameworks (e.g., google.*, zope.*).
'''



'''
Q5. (Coding scenario)
Suppose this structure:

mypkg/
    __init__.py
    utils.py

tools/
    analysis.py

# Fill in blanks:

# Import utils module
from ______ import utils

# Import analysis module
import ______
'''
# Import utils module
from mypkg import utils
print(utils)   # <module 'mypkg.utils' ...>

# Import analysis module
import tools.analysis
print(tools.analysis)   # <module 'tools.analysis' ...>

'''
Explanation:
- `from mypkg import utils` → imports the `utils.py` module inside the `mypkg` package.  
- `import tools.analysis` → imports the `analysis.py` module inside the `tools` package.  
- Both are valid because `mypkg` has `__init__.py` (a package), and `tools` is also treated as a package with submodules.  
'''



'''
📌 Key Shorthands

- Module = single .py file  
- Package = directory + __init__.py  
- Namespace Package = directory (no __init__.py), can span multiple paths
'''
