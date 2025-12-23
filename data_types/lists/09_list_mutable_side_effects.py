'''
Q1. What are mutable side effects?
Ans. Mutable side effects happen when a function modifies a list passed to it.
'''
# Example
def bad_function(lst):
    lst.clear()   # mutates original list

data = [10, 20, 30]
bad_function(data)
# data = []  ❗ unexpected for beginners


'''
Q2. How can you avoid mutable side effects?
Ans. By working on a COPY of the list instead of the original.
'''
# Example
def safe_function(lst):
    temp = lst.copy()
    temp.append(99)
    return temp

data = [1, 2, 3]
new_data = safe_function(data)
# data     = [1, 2, 3]
# new_data = [1, 2, 3, 99]
