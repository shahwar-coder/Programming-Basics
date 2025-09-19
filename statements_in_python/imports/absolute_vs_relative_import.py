'''
📌 Absolute vs Relative Imports

1. Absolute
   • Full path from project root
   • Example: from mypackage import module_a
   • ✅ Clear, works everywhere

2. Relative
   • Use . / .. for current/parent package
   • Example: from .. import module_a
   • ⚠ Only works inside packages (not top-level scripts)

3. Pitfalls
   • Relative fails in scripts (python file.py)
   • Too many dots = unreadable
   • Mixing styles = confusion

4. Best Practices
   • Prefer absolute for clarity
   • Use relative only for nearby modules
   • Keep style consistent in project
'''


'''
Q1. What is the difference between absolute and relative imports?
Ans:
- Absolute = full path from project root.
- Relative = use . / .. to refer to current/parent package.

Example:
# Absolute
from mypkg import utils

# Relative (inside mypkg/subpkg/module.py)
from .. import utils



Q2. Why are absolute imports preferred?
Ans:
- Always clear where a module comes from.
- Work consistently in all contexts (script, package, REPL).

Example:
from mypkg.subpkg import helper   # ✅ no ambiguity



Q3. When can relative imports fail?
Ans:
- When you run a module directly as a script (python file.py).
- Python treats it as __main__ → no package context → ImportError.

Example:
# Inside mypkg/subpkg/module.py
from .. import utils   # ❌ fails if run directly: python module.py



Q4. What are the readability pitfalls of relative imports?
Ans:
- Too many dots become confusing.
- Mixing absolute and relative imports makes maintenance harder.

Example:
from ....tools import parser   # ❌ hard to read, fragile



Q5. What is the best practice for imports?
Ans:
- Prefer absolute imports for clarity.
- Use relative only for short, local references (one dot).
- Stay consistent across the project.
'''
