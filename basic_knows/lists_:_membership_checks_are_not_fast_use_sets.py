'''
Q. Are membership checks (x in lst) fast?
Ans:
No — `in` performs a **linear search** in lists → O(n).  
For faster membership checks, use **sets**, which provide **O(1)** average time lookup.
'''

# Example with list (slow for large data)
lst = [1, 2, 3, 4, 5]
print(5 in lst)        # True (checks each element)
print(100 in lst)      # False (scans all elements)

# Example with set (much faster for lookups)
s = {1, 2, 3, 4, 5}
print(5 in s)          # True (hash lookup, O(1))
print(100 in s)        # False (immediate check)

# Demonstration for large collections
large_list = list(range(1_000_000))
large_set = set(range(1_000_000))

# Checking membership
print(999_999 in large_list)   # Slower → linear scan
print(999_999 in large_set)    # Faster → constant time
'''

✅ Summary:
- `in` with **list/tuple** → O(n) time (linear search)
- `in` with **set/dict** → O(1) average time (hash-based lookup)
- Prefer sets when frequent membership testing is required.
'''
