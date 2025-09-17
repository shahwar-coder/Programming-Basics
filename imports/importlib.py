'''
Q1. What does importlib.import_module() do?
Ans: Imports a module given its name as a string.  
Supports dotted paths too.
'''
# Example 1 (simple):
import importlib
math_mod = importlib.import_module("math")
print(math_mod.sqrt(16))   # 4.0

# Example 2 (dotted path):
import importlib
json_decoder = importlib.import_module("json.decoder")
print(json_decoder.JSONDecoder)   # <class 'json.decoder.JSONDecoder'>

'''
Explanation:
- "json.decoder" is a submodule inside the standard library's json package.
- importlib.import_module("json.decoder") gives you the decoder module object.
- From there, you can access classes/functions like JSONDecoder directly.
'''



'''
Q2. Why prefer importlib.import_module() over __import__()?
Ans: It's higher-level, more readable, and safer.  
It’s the modern API for dynamic imports.
'''



'''
Q3. What does importlib.reload(module) do?
Ans: Re-executes the module’s code in place, resetting its state.  
Useful in REPL/dev workflows, but can cause side effects 
if other parts of the program hold references.

Example:
'''
import importlib, math
math = importlib.reload(math)   # reloaded



'''
Q3. What does importlib.reload(module) do?
Ans: Re-executes the module’s code in place, resetting its state.  
Useful in REPL/dev workflows, but can cause side effects 
if other parts of the program hold references.

Example:
'''
import importlib, math
math = importlib.reload(math)   # reloaded



'''
Q4. What are common use cases of importlib utilities?
Ans:
- Plugin systems (load modules by name at runtime)
- Reloading code during development
- Safer dynamic imports than using __import__()

Let's see each one of them one by one:
'''
'''
1>PLUGIN SYSTEMS:
-> Load a module dynamically by string (e.g., user config decides which plugin to load)
'''
import importlib

plugin_name = "math"   # could come from config/user input
plugin = importlib.import_module(plugin_name)

print(plugin.sqrt(81))   # 9.0

'''
2>RELOADING CODE DURING DEVELOPMENT:
-> Useful when you tweak a file without restarting Python
'''
import importlib, mymodule

# change mymodule.py file in editor...
importlib.reload(mymodule)   # re-executes updated code

'''
3>Safer dynamic imports than __import__()
'''
import importlib

json_decoder = importlib.import_module("json.decoder")
print(json_decoder.JSONDecoder)   # <class 'json.decoder.JSONDecoder'>

'''
Summary of the utilities:
- Plugin systems → runtime flexibility.
- Reloading → fast iteration in REPL/dev.
- Safer imports → cleaner than __import__(), especially for dotted paths.
'''

