'''
Q1. What is an integer (int) in Python?
Ans:
An integer is a whole number with no fractional part.  
It can be positive, negative, or zero.  
Python integers have *arbitrary precision* — limited only by memory.
'''
# Example
x = 42
y = -10
print(type(x), x + y)   # <class 'int'> 32



'''
Q2. What are the different ways to represent integers in Python?
Ans:
Integers can be written in multiple numeral systems:
- Decimal → 42  
- Binary → 0b101010  
- Octal → 0o52  
- Hexadecimal → 0x2A
'''
# Example
print(0b101010, 0o52, 0x2A)   # 42 42 42



'''
Q3. What are the basic arithmetic operations supported by int?
Ans:
+, -, *, //, %, **  
- `//` → floor division  
- `%` → remainder  
- `**` → exponentiation
'''
# Example
a, b = 7, 3
print(a + b, a - b, a * b, a // b, a % b, a ** b)
# Output: 10 4 21 2 1 343



'''
Q4. What are bitwise operations for integers?
Ans:
They operate on the binary representation of numbers:
- &  → AND  
- |  → OR  
- ^  → XOR  
- ~  → NOT  
- << → left shift  
- >> → right shift
'''
# Example
x, y = 5, 3
print(x & y, x | y, x ^ y, ~x, x << 1, x >> 1)
# Output: 1 7 6 -6 10 2



'''
Q5. What built-in functions are commonly used with integers?
Ans:
- `abs(x)` → absolute value  
- `pow(x, y[, mod])` → power with optional modulus  
- `divmod(a, b)` → returns (quotient, remainder)  
- `bin(x), oct(x), hex(x)` → convert to different bases  
- `round(x[, n])` → rounds number (works mainly with floats)
'''
# Example
print(abs(-5), pow(2, 5), pow(2, 5, 3), divmod(10, 3))
print(bin(10), oct(10), hex(10))
# Output: 5 32 2 (3, 1) 0b1010 0o12 0xa



'''
Q6. What happens when integers mix with floats in expressions?
Ans:
If an int and a float are used together,  
Python automatically promotes the result to a float.
'''
# Example
x = 5 + 2.0
print(x, type(x))   # 7.0 <class 'float'>



'''
Q7. Are integers mutable or immutable?
Ans:
Integers are *immutable*.  
Any operation that changes their value creates a new object in memory.
'''
# Example
x = 10
print(id(x))
x += 1
print(id(x))   # different id → new object created



'''
Q8. Can integers overflow like in C or Java?
Ans:
No! Python automatically expands integer size as needed.  
There’s no overflow — only memory limits.
'''


'''
Q9. What’s the difference between / and // for integers?
Ans:
- `/` → true division → always gives a float  
- `//` → floor division → gives the integer quotient
'''
# Example
print(7 / 2)   # 3.5
print(7 // 2)  # 3



'''
Q10. What happens with bitwise NOT (~) for integers?
Ans:
It inverts all bits of the number —  
mathematically equivalent to `-(x + 1)`.
'''
# Example
print(~5)   # -6
print(~0)   # -1
