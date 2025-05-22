'''
List:
- collection of arbitrary objects
- ordered
- mutable
'''

# Example of simple list:
numbers=[1,2,3]
print(f"Numbers : {numbers}, Type : {type(numbers)}")

# Example of mixed list:
mixed=['a', True, 23, None]
print(f"Mixed : {mixed} , Type : {type(type(mixed))}")

# Creating a list
# way 1:
numbers=[1,2,3,4]
print(f"Numbers: {numbers}")

# way 2:
characters = list("hello")
print(f"Word split into characters : {characters}")

# way 3:
duplicates = [5] * 11
print(f"Duplicates : {duplicates}")
