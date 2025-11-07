'''
Q. Can slicing be used to copy lists?
Ans:
Yes — using `lst[:]` creates a **shallow copy** of the list.
'''
# Example
a = [1, 2, 3]
b = a[:]        # copy
b.append(4)
print(a, b)     # [1, 2, 3] [1, 2, 3, 4]
