'''
Q1. Why should nesting be minimized?
Ans:
- Deep nesting makes logic hard to read and debug.
- Flat structure using `elif`, `and`, or early return improves clarity.
'''

# ❌ Too nested
if a:
    if b:
        if c:
            print("All true")

# ✅ Better
if a and b and c:
    print("All true")



'''
Q2. Quick shorthand
✔ Use nesting only when logically dependent  
✔ Too much nesting → harder maintenance  
✔ Prefer logical ops, elif, or early exits  
✔ Indentation decides scope of else
'''
