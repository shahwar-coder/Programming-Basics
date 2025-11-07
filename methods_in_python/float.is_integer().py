'''
Q. What is the use of float.is_integer()?
Ans:
It checks if a float value is **mathematically an integer**,  
even though its type is still float.
'''
# Example
print((3.0).is_integer())   # True
print((3.1).is_integer())   # False
print((-7.0).is_integer())  # True
