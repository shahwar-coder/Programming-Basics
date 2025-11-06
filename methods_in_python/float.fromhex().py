'''
Q. How do you convert a hex string back to a float?
Ans:
Use `float.fromhex()` — it converts a hexadecimal string  
produced by `.hex()` back to the exact same float.
'''
# Example
print(float.fromhex('0x1.8p-1'))  # 0.75
print(float.fromhex('0x1.c000000000000p+1'))  # 3.5
