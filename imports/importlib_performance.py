'''
Q1. How does importlib help with performance?
Ans: importlib.import_module enables on-demand imports by string name,  
useful for plugins and conditional loading.

Example:
'''
import importlib
math_mod = importlib.import_module("math")
print(math_mod.sqrt(25))

# Step-by-step:
# 1. math is not imported until import_module is called.
# 2. Then sqrt(25) runs successfully.

# ÷-> Here we did not need to import at top level of the module, when we needed we just imported and used.



'''
Q2. How to profile import performance in Python?
Ans:
- Use built-in flag: python -X importtime script.py
- Shows per-module timings.
- For deeper analysis, use profilers like py-spy or scalene.

Example:
'''
$ python -X importtime myscript.py
# Output shows how long each import took.



'''
Q3. What are best practices for import-time optimization?
Ans:
- Only import what’s needed.
- Lazy-load heavy modules.
- Use conditional imports for optional dependencies.
- Profile before optimizing — don’t guess.
'''
