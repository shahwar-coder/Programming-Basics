'''
__hash__ : a fast “number fingerprint” for an object.
You don't keep searching, the `number fingerprint` leads you.

In Leyman terms you can say, `__hash__ is a method that turns an object into a number.`
Same object --> same number
That number helps Python store and find things fast

__hash__ is required in Python because Python has hash-based-collections:
like-> dicts and sets,
they need to store/find things instantly

Instead of searching item-by-item (which is slow ofcourse)
Python calls --> __hash__() --> Gets a Number --> Jumps directly to right place

__hash__ tells Python WHERE to look
__eq__ tells Python IS it really the same
'''

# Example 1
fruits = set()
fruits.add("apple")
fruits.add("apple")

print(fruits)

# Output  : {'apple'}

# '''
# # Key Points (What This Example Shows)
# - `set()` creates an unordered collection of UNIQUE elements.
# - Calling `add("apple")` twice does not create duplicates.
# - Sets automatically remove duplicates for you.

# # Why This Happens
# - A set checks if an element already exists before adding it.
# - Since "apple" is already present, the second add is ignored.

# # Output Explanation
# - Only one "apple" appears in the set:
#   {'apple'}

# # Backend Perspective
# - Sets are ideal for:
#   - Deduplication
#   - Membership checks (fast: O(1))
#   - Enforcing uniqueness constraints
# - Common use cases:
#   - Unique user IDs
#   - Unique tags
#   - Removing duplicates from lists

# # Core Takeaway
# - Lists allow duplicates.
# - Sets guarantee uniqueness by design.
# '''



# Example 2
scores = {}
scores["math"] = 95
scores["math"] = 100

print(scores)

# Output : {'math': 100}

# '''
# # Key Points (What This Example Shows)
# - Dictionaries store data as key → value pairs.
# - Keys in a dictionary must be UNIQUE.
# - Assigning a value to an existing key overwrites the old value.

# # Why This Happens
# - "math" is used as the key both times.
# - The second assignment:
#     scores["math"] = 100
#   replaces the previous value (95).

# # Output Explanation
# - The dictionary keeps only the latest value for a key:
#   {'math': 100}

# # Backend Perspective
# - Dicts behave like a key-based lookup table.
# - Very common in:
#   - Configuration objects
#   - Request payloads
#   - Caches
#   - Database row representations
# - Overwriting is intentional and deterministic.

# # Comparison With Other Structures
# - list  → allows duplicate values
# - set   → enforces unique values
# - dict  → enforces unique KEYS, values can change

# # Core Takeaway
# - Dictionary keys are unique.
# - Reassigning a key updates its value, it does not create duplicates.
# '''



