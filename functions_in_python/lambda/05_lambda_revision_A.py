'''
Q1. What is a lambda function in Python?
A.
A lambda function is a small, anonymous function written in one line.
It is used when you need a simple function quickly without giving it a name.
'''
# Example:
# add = lambda a, b: a + b
# add(2, 3) → 5


'''
Q2. How is a lambda function different from a normal def function?
A.
A lambda has no name, no return keyword, and can contain only one expression.
A def function can have multiple lines and statements.
'''
# Example:
# def square(x):
#     return x * x
#
# square_lambda = lambda x: x * x


'''
Q3. What is the general syntax of a lambda function?
A.
The syntax is:
lambda arguments : expression
The expression is evaluated and returned automatically.
'''
# Example:
# lambda x: x * 2
# lambda a, b: a + b


'''
Q4. When should lambda functions be used?
A.
Lambda functions should be used for short, simple logic that is used only once
or passed directly as an argument to another function.
'''
# Example:
# sorted(data, key=lambda x: x[1])


'''
Q5. How are lambda functions commonly used with map() and filter()?
A.
Lambda functions are often passed to map() to transform elements
and to filter() to keep elements based on a condition.
'''
# Example:
# list(map(lambda x: x * x, [1, 2, 3])) → [1, 4, 9]
# list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) → [2, 4]


'''
Q6. Can conditional logic be used inside a lambda function?
A.
Yes, lambda supports conditional expressions using the ternary form,
but it does not support if-statements or loops.
'''
# Example:
# label = lambda age: "Adult" if age >= 18 else "Minor"
# label(20) → "Adult"
