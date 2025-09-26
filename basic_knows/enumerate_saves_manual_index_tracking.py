'''
enumerate() in Python:
    - Used in for-loops when you need index + value.
    - Saves you from manually tracking index.
'''
# Example:
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

