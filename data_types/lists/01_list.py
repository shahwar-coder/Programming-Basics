'''
Q1. What is a list in Python?
Ans:
A **list** is a **mutable**, ordered, and dynamic sequence used to store multiple items.  
It can contain elements of **different types** — numbers, strings, even other lists.
'''
# Example
nums = [1, 2, 3]
mix = [10, "Hi", 3.5, True]
print(nums, mix)
# [1, 2, 3] [10, 'Hi', 3.5, True]



'''
Q2. What does "mutable" mean for lists?
Ans:
It means lists can be **changed in place** — you can modify, add, or remove items  
without creating a new list.
'''
# Example
data = [1, 2, 3]
data[1] = 20
print(data)   # [1, 20, 3]



'''
Q3. How do you create a list in Python?
Ans:
You can create lists using:
1️⃣ Square brackets `[ ]`  
2️⃣ The `list()` constructor
'''
# Example
a = [1, 2, 3]
b = list("abc")
c = list(range(5))
print(a, b, c)
# [1, 2, 3] ['a', 'b', 'c'] [0, 1, 2, 3, 4]



'''
Q4. What is meant by "ordered" sequence?
Ans:
List elements keep their **insertion order**,  
so you can access them by index (`list[i]`).
'''
# Example
letters = ['a', 'b', 'c']
print(letters[0], letters[-1])  # 'a' 'c'



'''
Q5. What happens when you modify one list element?
Ans:
Only that element changes — Python doesn’t copy the whole list.  
Mutations affect the original list directly.
'''
# Example
nums = [1, 2, 3]
nums[0] = 99
print(nums)  # [99, 2, 3]


'''
Q6. How are lists different from tuples?
Ans:
- **List** → mutable, defined with `[ ]`  
- **Tuple** → immutable, defined with `( )`
'''


'''
Q7. What happens when you pass a string to list()?
Ans:
It converts each **character** in the string into a separate list element.
'''


'''
Q8. Can you nest lists inside lists?
Ans:
Yes — lists can contain other lists (nested lists).  
They’re often used to represent tables, grids, or matrices.
'''
# Example
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3
