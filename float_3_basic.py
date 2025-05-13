'''
Key methods or attributes of float:

1. as_integer_ratio : numerator/denominator == x
2. hex() : hex string representation
3. fromhex() : back to decimal
4. is_integer() : Ture is float is exactly an integer
'''

# as_integer_ratio
x=0.75
print(x.as_integer_ratio()) # 3/4

y=2.5
print(y.as_integer_ratio()) # 5/2

# hex()
x=0.1
print(x.hex()) # 0x1.999999999999ap-4

# fromhex()
print(float.fromhex('0x1.999999999999ap-4')) # 0.1

# is_integer
x=3.0
print(x.is_integer()) #True

x=3.5
print(x.is_integer())

