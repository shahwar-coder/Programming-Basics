'''
Q1. Where does Python look for installed vs local code?
Ans:
- Installed packages live in site-packages (inside venv or global install).
- Local source files are found via current directory or PYTHONPATH.

Example:
'''
import math, sys
print("math origin:", math.__file__)   # built-in, no file
import json
print("json origin:", json.__file__)   # stdlib

# Step-by-step:
# 1. Built-in modules like math may not have __file__.
# 2. stdlib/imported modules show actual path.

# math origin: /usr/lib/python3.8/lib-dynload/math.cpython-38-x86_64-linux-gnu.so
# json origin: /usr/lib/python3.8/json/__init__.py



'''
Q2. What is the difference between flat layout and src layout?
Ans:
- Flat layout = project/mypkg/ → works, but imports may "accidentally" succeed
  because Python’s current working directory is in sys.path.
- src layout = project/src/mypkg/ → prevents accidental imports, 
  ensuring your package is only found once properly installed (or via -e).

Flat layout (❌ risky):
project/
│
├── mypkg/        # your package
│   └── __init__.py
└── tests/
    └── test_file.py

# Problem:
# Running "python tests/test_file.py" may import mypkg/ directly,
# even if the package isn’t installed. CI might pass locally but fail after install.


Src layout (✅ preferred):
project/
│
├── src/
│   └── mypkg/      # your package
│       └── __init__.py
└── tests/
    └── test_file.py

# Benefit:
# "mypkg" isn’t on sys.path unless installed (or installed with -e).
# Prevents accidental local imports and catches packaging issues early.

Step-by-step benefits of src layout:
1. Forces you to test your package as installed, not just as local files.
2. Prevents name clashes (local "mypkg" won’t shadow stdlib or other packages).
3. Matches modern Python packaging best practices (PEP 621, pyproject.toml).
'''



'''
Q3. What is an editable install, and why is it better than PYTHONPATH?
Ans:
- pip install -e . creates a link from site-packages to your source.
- Edits in source reflect immediately in imports.
- PYTHONPATH works but is fragile and error-prone.

Example:
$ pip install -e .
# Step-by-step:
# 1. Creates link in site-packages.
# 2. Importing mypkg uses your live source code.
'''



'''
Q4. How does installation affect import behavior?
Ans:
- Running a module directly (python file.py) can break relative imports.
- Correct way: python -m package.module
- Local files with same name can shadow stdlib or installed packages.

Example:
# If you create a file json.py in your project,
# import json will load your file, not stdlib json.
'''



'''
Q5. How can you debug where a module was imported from?
Ans: Check the __file__ attribute of the module.

Example:
import mypkg
print(mypkg.__file__)
# Step-by-step:
# 1. Shows actual file path.
# 2. Tells you if it came from src/, site-packages, or shadowed local file.
'''



'''
Q6. What are best practices for packaging & imports?
Ans:
- Use src layout to avoid accidental imports.
- Use virtualenvs for isolation.
- Prefer editable installs during development.
- Don’t rely on modifying sys.path or PYTHONPATH.
- Test as installed (or editable) in CI for consistency.
'''
