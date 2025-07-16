'''
- for
- for loop is used to iterate iver a sequence
- and run a block of code for each iteration
- it's like saying for each item in the sequence/group "do something"
'''

# BASIC SYNTAX
iterable=[1,2,3]
for variable in iterable:
    # do something with variable
    pass

# SIMPLE EXAMPLE
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping over a range
for i in range(5):
    print(i) # 0->4

# ENUMERATE (when we want to use index and value)
for index, value in ['apple', 'berry', 'cherry']:
    print(f"Index : {index}, Value : {value}")

# ZIP (to do parallel looping)
names=['shahwar', 'alam', 'naqvi']
scores=[30,50,70]

for name, score in zip(names, scores):
    print(f"{name} scored -> {score}")


'''
- break helps in breaking from the loop
- continue helps in skipping the iteration
- else can also be used with for, see example below.
- else part executes
'''

nums = [1, 2, 3, 4]

for num in nums:
    if num == 0:
        print("Found 0!")
        break
else:
    print("No zero found.")

# OUTPUT
# No zero found


