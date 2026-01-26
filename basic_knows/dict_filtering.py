'''
- Filtering a dict means selecting only a fixed, required set of keys.
- The source dict may contain many keys, but we extract only what we need.
- A predefined list/set (FIELDS) acts as the filter rule.
- Dict comprehension creates a new dict with only allowed keys.
- product.get(key) safely fetches values without raising KeyError.
- Missing keys return None instead of breaking the code.
- Original data remains unchanged (non-mutating operation).
- Looping over a list of dicts applies the same filter consistently.
- Improves data cleanliness for UI, API responses, or storage.
- Makes code explicit, readable, and easy to maintain.
'''

'''
Example: filtering a dict using a fixed set of required keys
'''

FIELDS = {"id", "name", "price"}  # allowed / required keys

products = [
    {"id": 1, "name": "Laptop", "price": 900, "stock": 12, "rating": 4.5},
    {"id": 2, "name": "Mouse", "price": 20, "color": "black"},
]

filtered_products = [
    {key: product.get(key) for key in FIELDS}
    for product in products
]

print(filtered_products)
