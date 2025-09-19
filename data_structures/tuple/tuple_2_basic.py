'''
- tuples can contain negative values
- negative values are helppful in custom sorting, rank priorities, store structured data
- `-ve` tuple value invites the decending order (very useful) 
'''

# Let's see an example to understand

# Run 1:
students = [
    ("Ali", 82),
    ("Zara", 91),
    ("Omar", 75)
]
students.sort()
print(f"Default Sort : {students}") # Will by default sort by names in ascending order

# Run 2 (with keys):
students = [
    ("Ali", 82),
    ("Zara", 91),
    ("Omar", 75)
]
students.sort(key= lambda student: student[1]) # ascending order
print(f"Ascending Order : {students}")

students.sort(key= lambda student: -student[1]) # descending order
print(f"Descending Order : {students}")
