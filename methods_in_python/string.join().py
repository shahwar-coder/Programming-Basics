'''
Q. What does join() do?
Ans:
`join(iterable)` combines elements of an iterable (like a list, tuple, or generator)
into a single string, inserting the calling string as a separator.
All elements must be strings — not numbers or other types.
'''
# Example 1: Basic usage
words = ["Python", "is", "awesome"]
print(" ".join(words))     # "Python is awesome"
print("-".join(words))     # "Python-is-awesome"

# Example 2: Joining characters
chars = ['H', 'e', 'l', 'l', 'o']
print("".join(chars))      # "Hello"
print("*".join(chars))     # "H*e*l*l*o"

# Example 3: Joining with newline
lines = ["line1", "line2", "line3"]
print("\n".join(lines))
# Output:
# line1
# line2
# line3

# Example 4: Joining file path components
folders = ["home", "user", "downloads"]
print("/".join(folders))   # "home/user/downloads"

# Example 5: Joining tuple elements
t = ("2025", "11", "07")
print("-".join(t))         # "2025-11-07"

# Example 6: Joining list of numbers after type conversion
nums = [1, 2, 3]
print(", ".join(map(str, nums)))   # "1, 2, 3"

# Example 7: Joining empty list
empty = []
print(" ".join(empty))     # "" (empty string)

# Example 8: Using join() with generator expression
print(", ".join(word.upper() for word in ["python", "rocks"]))
# "PYTHON, ROCKS"

