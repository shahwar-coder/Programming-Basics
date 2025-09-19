'''
Q1. What is sys.meta_path used for?
Ans: It's a list of "finders" that Python checks during import.  
You can insert custom finders to control how modules are located.

Example:
'''
import sys
print(sys.meta_path)   # shows default finders (builtins, filesystem, etc.)



'''
Q2. What is the difference between a Finder and a Loader?
Ans:
- Finder → says "I can handle this module" (returns a spec).
- Loader → actually loads the module into memory from that spec.
'''



'''
Q3. How can you inspect a module's import spec?
Ans: Use importlib.util.find_spec().

Example:
'''
import importlib.util
spec = importlib.util.find_spec("math")
print(spec.name, spec.origin)
# Output: math built-in



'''
Q4. What are some real use cases for custom import hooks?
Ans:
- Plugin systems (load modules dynamically at runtime). (check advanced_imports_plugins.py)
- Importing from unusual sources (database, zip file, web).
- Debugging/tracing the import process.
'''
