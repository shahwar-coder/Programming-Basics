# map() with dictionaries (transform each dict)
data = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]
# Add a new key without mutating original dict
updated = list(map(lambda x: {**x, "country": "India"}, data))

# lambda x: {**x, "country": "India"}
# Key points about **x:
# - x is ONE dictionary from data at a time
# - **x unpacks (spreads) all key–value pairs of x into a new dict
# - This creates a COPY, not a modification of the original dict
# - Then "country": "India" is added/overwritten in the new dict
# - Original data remains unchanged (no mutation)
# - If x already had "country", the new value would replace it
