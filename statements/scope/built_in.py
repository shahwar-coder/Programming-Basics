'''
🔹 Built-in Scope (B):
- The outermost scope in Python, always available.
- Contains predefined names like:
  • Functions: len(), print(), type(), range(), max()
  • Exceptions: ValueError, KeyError
  • Constants: True, False, None

🔹 Example (using Built-in):
print(len("hello"))   # Finds 'len' in Built-in scope

🔹 Shadowing Built-ins:
len = 100
print(len("hi"))      # ❌ TypeError, 'len' is now int, not function

🔹 Fix by using 'builtins' module:
import builtins
print(builtins.len("hi"))   # ✅ 2

⚡ Key Point:
- Built-in scope is global across all Python modules.
- It is the last place Python checks if a name is not found in Local, Enclosing, or Global.
- Avoid shadowing built-in names to prevent bugs.
'''
