'''
Q. What does “structural” mean in structural pattern matching?
Ans:
It means Python looks at the *shape* or *structure* of the data —
like number of elements, keys, or attributes —
instead of just comparing plain values.
'''
# Example
point = (10, 20, 30)
match point:
    case (x, y): print("2D")
    case (x, y, z): print("3D")   # Matches because structure has 3 elements
