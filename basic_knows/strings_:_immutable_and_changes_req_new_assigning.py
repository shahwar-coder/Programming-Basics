'''
Q. What does "immutable" mean for strings and what follows?
Ans:
You cannot change a string in-place. Operations (replace, slice, concat) produce a **new** string.  
This makes strings safe to share but requires re-assignment for "changes".
'''
# Example
s = "cat"
s2 = s.replace("c", "b")  # new string created
print(s, s2)              # "cat" "bat"
# To 'change' s you must assign: s = s2
