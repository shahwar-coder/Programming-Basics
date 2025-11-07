'''
Q. What’s the recommended way to test truth in conditions?
Ans:
Use **direct truth checks**, not `== True` or `is True`.
'''
# Example
items = [1, 2, 3]
if items:          # ✅ Preferred
    print("List not empty")
if len(items) > 0: # 👎 Verbose
    print("Still works")
