def add(x, y): 
    return x + y
def mul(x, y): 
    return x * y

ops = {
    "add": add,   # maps "add" -> function add
    "mul": mul    # maps "mul" -> function mul
}

op = "mul"
print(ops.get(op, lambda *a: "bad op")(3, 4))  # 12

'''
=========== CODE ENDS HERE ==============
=========== CODE ENDS HERE ==============
=========== CODE ENDS HERE ==============
=========== CODE ENDS HERE ==============
'''


'''
For Detailed Explanation (revise)
'''
#!/usr/bin/env python3
"""
Step-by-step explanation of function dispatch using a dict map.

We will:
1) Define two functions: add(x, y) and mul(x, y).
2) Create a dict 'ops' that maps operation names (strings) to those functions.
3) Pick an operation name (here, "mul").
4) Look up the function from the dict using ops.get(key, default).
   - If the key exists, we get the function (e.g., mul).
   - If the key does NOT exist, we get the default function (a lambda returning "bad op").
5) Immediately CALL the returned function with arguments (3, 4).
6) Print the result.

Why dict-based dispatch?
- It replaces long if/elif chains with a clean, scalable lookup.
- It's easy to add new operations: just define a function and add one dict entry.
"""

# 1) Define two simple operations.
def add(x, y):
    """Return the sum of x and y."""
    return x + y

def mul(x, y):
    """Return the product of x and y."""
    return x * y

# 2) Map operation names to the actual function *objects* (not calling them yet).
ops = {
    "add": add,   # maps the string "add" to the function add
    "mul": mul    # maps the string "mul" to the function mul
}

# 3) Choose the operation name we want to perform.
op = "mul"

# 4) Use dict.get to retrieve a function by name.
#    - If 'op' is present in ops, we get that function (e.g., mul).
#    - If not, we fall back to a default lambda that accepts any args and says "bad op".
# 5) Immediately call the returned function with (3, 4).
#    NOTE: Parentheses grouping:
#       ops.get(op, default)       -> returns a FUNCTION
#       ( ... )(3, 4)              -> calls that function with arguments 3 and 4
result = ops.get(op, lambda *a: "bad op")(3, 4)

# 6) Print the result. For op="mul" and args (3, 4), we expect 12.
print(result)  # -> 12
