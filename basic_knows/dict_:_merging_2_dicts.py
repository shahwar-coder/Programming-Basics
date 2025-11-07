"""
📘 Summary: Merging Dictionaries in Python 3.9+

- The '|' operator merges two dictionaries into a new one.
- Does NOT modify the original dictionaries.
- If keys overlap, values from the right dictionary override.
"""
# Example:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# merged = dict1 | dict2
# Result: {'a': 1, 'b': 3, 'c': 4}
