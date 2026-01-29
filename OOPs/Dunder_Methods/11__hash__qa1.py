'''
Q1. What is __hash__ in simple terms?
A.
__hash__ is a method that turns an object into a fast numeric fingerprint.
Python uses this number to decide WHERE to store the object for quick lookup.
'''
# Example:
# hash("apple")
# → some integer number
# Same object/value → same hash number


'''
Q2. Why does Python need __hash__ at all?
A.
Because Python has hash-based collections like set and dict
that need instant storage and lookup instead of slow searching.
'''
# Example:
# Instead of checking every item:
# Python does → hash(key) → jump to the right bucket


'''
Q3. What role does __hash__ play in a set?
A.
__hash__ tells Python WHERE the item might belong.
__eq__ is used only if two items land in the same place.
'''
# Example:
# fruits = set()
# fruits.add("apple")
# fruits.add("apple")
# Output: {'apple'}


'''
Q4. Why are duplicates automatically removed in a set?
A.
Because equal items produce the same hash,
and Python confirms equality before inserting.
'''
# Example:
# "apple" and "apple"
# hash("apple") == hash("apple")
# → duplicate ignored


'''
Q5. How does __hash__ work with dictionaries?
A.
Dictionary keys are hashed to decide storage location.
If the same key is used again, the value is overwritten.
'''
# Example:
# scores = {}
# scores["math"] = 95
# scores["math"] = 100
# Output: {'math': 100}


'''
Q6. What is the division of responsibility between __hash__ and __eq__?
A.
__hash__ answers: "Where should I look?"
__eq__ answers: "Is this actually the same object?"
'''
# Example:
# Step 1: hash(key) → find bucket
# Step 2: __eq__ → confirm equality inside bucket
