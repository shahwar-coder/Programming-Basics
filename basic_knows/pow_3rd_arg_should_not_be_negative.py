'''
Q. What types of numbers does pow() work with?
Ans:
- Works with int and float.  
- The 3-argument form (mod) works only with integers and non-negative exponents.
'''
# Example
print(pow(2, 3.5))   # 11.313...
try:
    print(pow(2.0, 3.0, 5))
except TypeError as e:
    print("Error:", e)
# 11.313708498984761
# Error: pow() 3rd argument not allowed unless all arguments are integers
