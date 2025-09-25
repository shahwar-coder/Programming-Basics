'''
Q. How do you handle default/fallback with dict mapping?
Ans:
- Use `.get(key, default)` to avoid KeyError.

Example:
'''

color_map = {
    'r': 'Red',
    'g': 'Green',
    'b': 'Blue'
}

code = 'y'  # not in the dictionary
color = color_map.get(code, 'Unknown')

print(color)  # Output: Unknown
