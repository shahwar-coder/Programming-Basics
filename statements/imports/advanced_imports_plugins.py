'''
Q1. Why do we use plugins?
Ans: To make software extensible and decoupled.  
Plugins let you add new features at runtime without changing core code.

Example:
A text editor loads "spellcheck" or "theme" plugins at startup.
'''



'''
Q2. What are two common plugin discovery methods?
Ans:
1) Entry points → packaged plugins, discovered via importlib.metadata.entry_points
2) Directory discovery → load .py files from a "plugins/" folder dynamically
'''


'''
Q3. How does a simple directory-based plugin system work?
Ans:
- Each plugin defines a known function (e.g., register()).
- Loader scans plugin directory, imports each module, and calls register().
Example:
'''
# plugin_hello.py
def register():
    print("Hello plugin registered!")

# loader.py
import importlib.util, pathlib

for path in pathlib.Path("plugins").glob("*.py"):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.register()



'''
Q4. How do entry points help with plugins?
Ans: Entry points are metadata defined in a package’s setup.cfg/pyproject.toml.  
They let you discover installed plugins without scanning directories.

Example:
'''
from importlib.metadata import entry_points
print(entry_points(group="myapp.plugins"))
