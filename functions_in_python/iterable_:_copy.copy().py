'''
This type syntax:
'''
import copy
a = [1, 2, 3]
b = copy.copy(a)
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]

# OR below, syntax also works

'''
Q1. What happens when you assign one list to another using `=`?
Ans:
It **does not create a copy** — both variables point to the **same list** in memory.  
So, modifying one will affect the other.
'''
# Example
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)     # [1, 2, 3, 4] [1, 2, 3, 4]
print(a is b)   # True (same object)

'''
Q2. What is a shallow copy in Python?
Ans:
A **shallow copy** creates a **new outer container** (new list),
but the **inner (nested) objects are still references** to the same memory.  
So, if you modify a *nested object*, both copies see the change.

Why does this happen?
Because `.copy()` only duplicates the top-level list structure,  
not the elements inside it (which are still shared references).
'''
# Example 1: Nested list behavior
a = [[1, 2], [3, 4]]
b = a.copy()      # shallow copy → outer list copied, inner lists shared

print("Before change:")
print("a:", a)
print("b:", b)

b[0][0] = 99      # modifies the shared inner list

print("\nAfter modifying b[0][0]:")
print("a:", a)    # a also changes → [[99, 2], [3, 4]]
print("b:", b)    # b → [[99, 2], [3, 4]]
print(a is b)     # False (different outer lists)
print(a[0] is b[0])  # True (same inner list)



'''
Q3. How do you confirm if two lists share memory?
Ans:
Use the **identity operator** `is` or compare inner elements’ memory references.
'''
# Example
a = [[1], [2]]
b = a.copy()
print(a is b)       # False (different lists)
print(a[0] is b[0]) # True (same inner list)
