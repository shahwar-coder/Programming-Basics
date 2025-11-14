'''
Q1. What are the two main methods for string formatting in Python?
Ans:
Python mainly uses:
1) f-strings → f"{value}" (modern, fastest, most readable)
2) str.format() → "Hello {}".format(value) (flexible, older style)
'''
# Example
name = "Bob"
print(f"Hello {name}")
print("Hello {}".format(name))



'''
Q2. What are common formatting modifiers used with {value:...}?
Ans:
- .2f → round to 2 decimals
- ,   → thousand separator
- <10 → left-align in width 10
- ^10 → center-align in width 10
- b   → binary
- x   → hexadecimal
'''
# Example
n = 1234.567
print(f"{n:.2f}")    # 1234.57
print(f"{n:,}")      # 1,234.567
print(f"{15:b}")     # 1111



'''
Q3. How does str.format() work with positional and named placeholders?
Ans:
You can pass values by position or by keyword.
'''
# Example
print("{} {}".format("Hello", "World"))
print("{0} {1}".format("Hi", "There"))
print("{name} is {age}".format(name="Alice", age=30))



'''
Q4. When should you prefer f-strings over str.format()?
Ans:
Use f-strings when using Python 3.6+ because they are:
- More readable
- Faster
- Allow in-place expressions
Use str.format() only for older Python versions or advanced templates.
'''
# Example
price = 49.99
print(f"Price: {price:.2f}")   # preferred modern style



'''
Q5. How do you align text using formatting?
Ans:
Use <, >, ^ with a width number:
< → left-align
> → right-align
^ → center-align
'''
# Example
print(f"{'Hi':<10}END")   # Hi        END
print(f"{'Hi':^10}END")   #    Hi     END



'''
Q6. Can you format integers as binary, octal, or hex?
Ans:
Yes—use :b, :o, :x inside {} to convert numbers into bases.
'''
# Example
print(f"{10:b}")  # 1010
print(f"{10:o}")  # 12
print(f"{10:x}")  # a

print(f"{255:x}")    # ff
