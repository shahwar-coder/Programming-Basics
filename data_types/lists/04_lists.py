'''
Q1. What does the + operator do with lists?
Ans:
It **concatenates** (joins) two or more lists into a new one.  
The original lists remain unchanged.
'''
# Example
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]
print(a)  # [1, 2, 3]  (unchanged)



'''
Q2. What does the * operator do with lists?
Ans:
It **repeats** the elements of the list a given number of times.  
This creates a new list without modifying the original.
'''
# Example
nums = [1, 2]
print(nums * 3)    # [1, 2, 1, 2, 1, 2]
print(['Hi'] * 4)  # ['Hi', 'Hi', 'Hi', 'Hi']
