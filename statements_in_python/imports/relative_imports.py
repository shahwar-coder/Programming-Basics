'''
Q1. What does a single dot (.) mean in a relative import?
Ans: It refers to the current package.

Example:
'''
# in mypkg/subpkg/module.py
from . import helper   # imports mypkg/subpkg/helper.py




'''
Q2. What does two dots (..) mean in a relative import?
Ans: It refers to the parent package.

Example:
'''
# in mypkg/subpkg/module.py
from .. import utils   # imports mypkg/utils.py




'''
Q3. Can relative imports be used in top-level scripts?
Ans: No. They only work inside packages.  
Running a module as __main__ directly breaks relative imports.  
They need package context.
'''
'''
Let this be a package structure:
-> mypkg/
     __init__.py
     utils.py
     subpkg/
         __init__.py
         module.py

-> utils.py
   def helper():
     return "Hello from utils"

-> subpkg/module.py
   from .. import utils   # relative import from parent package
   def call_utils():
       return utils.helper()

CASE 1 (run as a package) ✅
python -m mypkg.subpkg.module

Output: 
Hello from utils

CASE 2 (run directly) ❌
python mypkg/subpkg/module.py

Output:
ImportError: attempted relative import with no known parent package
'''

'''
Explanation:
- When run directly, module.py becomes __main__, not part of "mypkg".
- Python doesn’t know what the "parent package" is.
- Relative imports need the package context, which is missing here.
'''



'''
Q4. What’s the main advantage and drawback of relative imports?
Ans:
- Advantage: Handy for intra-package references (less typing).
- Drawback: Multiple dots hurt readability; absolute imports are clearer.
'''
