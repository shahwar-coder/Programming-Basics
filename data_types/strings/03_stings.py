'''
Q1. What are f-strings in Python?
Ans:
F-strings (introduced in Python 3.6) are **formatted string literals**.  
They let you embed variables and expressions directly inside `{}`.
'''
# Example
name = "Shahwar"
score = 95
print(f"Hello {name}, your score is {score}.")       # Hello Shahwar, your score is 95.
print(f"{name.upper()} scored {score/100:.0%}")      # SHAHWAR scored 95%



'''
Q2. What are the benefits of using f-strings?
Ans:
✅ Fast and readable  
✅ Support expressions inside `{}`  
✅ Handle formatting (like precision, alignment, percentages) directly.
'''
# Example
price = 199.999
print(f"Price: ${price:.2f}")   # Price: $200.00
print(f"{2 + 3 = }")            # Prints expression with value (Python 3.8+)



'''
Q3. What does the format() method do?
Ans:
The `.format()` method replaces `{}` placeholders in a string  
with the values passed as arguments or keywords.
'''
# Example
name = "Aisha"
age = 21
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {1} and I am {0} years old.".format(age, name))
print("Coordinates: {x}, {y}".format(x=10, y=20))



'''
Q4. What are some advantages of format() over f-strings?
Ans:
It’s more **dynamic** — you can:
- Reorder or reuse placeholders  
- Pass variables dynamically  
- Use dictionary or object attributes for values
'''
# Example
data = {"lang": "Python", "ver": 3.12}
print("Using {lang} version {ver}".format(**data))  # Using Python version 3.12



'''just good to know
Q6. What are common format specifiers in % formatting?
Ans:
- `%s` → string  
- `%d` → integer  
- `%f` → float  
- `%.2f` → float with 2 decimal places
'''
# Example
name, marks = "Ali", 88.675
print("Student: %s, Marks: %.1f" % (name, marks))  # Student: Ali, Marks: 88.7



'''
Q7. How does format() handle alignment and width?
Ans:
You can control alignment using `<`, `>`, `^` and specify width after `:` inside `{}`.
'''
# Example
print("{:<10}".format("left"))   # 'left      '
print("{:^10}".format("center")) # '  center  '
print("{:>10}".format("right"))  # '     right'



'''
Q8. How can you format numbers in f-strings?
Ans:
Use format specifiers after a colon `:` inside `{}` —  
for example, decimals, commas, percentages, etc.
'''
# Example
n = 12345.6789
print(f"{n:,.2f}")   # "12,345.68"
print(f"{n:.1f}")    # "12345.7"
print(f"{n:.0%}")    # "1234568%"



'''
Q9. Which formatting method is preferred today?
Ans:
✅ **f-strings** — they’re modern, fast, and easy to read.  
`format()` is still useful for dynamic and complex templates.  
`%` formatting is mostly for backward compatibility.
'''
# Example
name = "Laila"
score = 92
print(f"{name} scored {score}%")              # Recommended
print("Result: {}%".format(score))            # Alternative
print("Score: %d%%" % score)                  # Old style
