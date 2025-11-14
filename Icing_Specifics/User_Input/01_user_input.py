'''
Q1. What does the input() function do in Python?
Ans:
input() pauses the program and waits for the user to type something.
It always returns the entered value as a STRING, no matter what the user types.
'''
# Example
name = input("Enter your name: ")
print("Hello", name)



'''
Q2. How do you display a prompt message using input()?
Ans:
You can pass a string message inside input() to guide the user
on what to type.
'''
# Example
age = input("Enter your age: ")



'''
Q3. Why is type conversion important with input()?
Ans:
Since input() always returns a string, convert data when you need
numbers using int(), float(), bool(), etc.
'''
# Example
num = int(input("Enter an integer: "))
price = float(input("Enter price: "))



'''
Q4. How do you take multiple inputs from a single line?
Ans:
Use split() to break the string into parts, then assign them
to multiple variables.
'''
# Example
x, y = input("Enter two items: ").split()
print(x, y)



'''
Q5. How do you take multiple numeric inputs using map()?
Ans:
Use map() to apply int() or float() to each split value.
'''
# Example
a, b = map(int, input("Enter two numbers: ").split())
print(a, b)



'''
Q6. How do you safely validate user input?
Ans:
Use try/except inside a loop to keep asking until valid input is given.
'''
# Example
while True:
    val = input("Enter a number: ")
    try:
        val = float(val)
        break
    except:
        print("Invalid, try again.")



'''
Q7. Why do input() values remain strings even if numbers are typed?
Ans:
input() reads raw text from the console; it can't guess your intended type.
Explicit conversion is required to avoid logic errors.
'''
# Example
data = input("Type 10: ")
print(type(data))  # <class 'str'>



'''
Q8. What happens if you convert invalid input using int() or float()?
Ans:
It raises a ValueError, so validation using try/except is essential 
when expecting numeric input from users.
'''
# Example
# int("abc") → ValueError



'''
Q9. Can split() handle multiple spaces or tabs between inputs?
Ans:
Yes, split() without arguments automatically handles any whitespace
(multiple spaces, tabs, newlines).
'''
# Example
a, b, c = input("Enter three values: ").split()



'''
Q10. Why is input() mainly used in small scripts and interactive programs?
Ans:
Because larger back-end or GUI applications take input from forms,
files, APIs, or databases—not directly from input(). It’s perfect
for beginners, learning, small tools, and terminal utilities.
'''
# Example
choice = input("Continue? (yes/no): ")
