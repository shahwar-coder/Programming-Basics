'''
📌 Simple Assignment (=)

1. Purpose
• Binds a name to an object (not copying the value)
x = 5    # x → 5

2. Multiple Targets
• Many names can point to the same object
a = b = []   
a.append(1)
print(b)   # [1]

3. Assignment Targets
• Can assign to variables, attributes, items, or slices
obj.attr = 10
person["name"] = "Alice"
nums[1:3] = [20, 30]

4. Rebinding vs Mutation
• Rebinding → name points to a new object
x = [1, 2]
x = [3, 4]      # x now points to a different list

• Mutation → change the object itself
x = [1, 2]
x.append(3)     # same list changed → [1, 2, 3]

• Mutation affects all names pointing to that object
a = b = [1]
a.append(2)
print(b)   # [1, 2]

5. Scope
• By default, assignment is local to the current function
x = 1
def f():
    x = 2   # local x, does not affect global x
'''

'''
Q1. What does the assignment operator (=) do in Python?
Ans: It binds a name to an object, not copying the value.  
Example: x = 5 → name x now refers to the integer object 5.

Q2. How does Python handle multiple targets in assignment?
Ans: Multiple names can be bound to the same object.  
Example: a = b = []  
If 'a' is mutated (a.append(1)), 'b' sees the change too, since 
both names point to the same list.

Q3. What are valid assignment targets in Python?
Ans: 
- Variables → x = 10  
- Attributes → obj.attr = 5  
- Items → person["name"] = "Alice"  
- Slices → nums[1:3] = [20, 30]

Q4. What is the difference between rebinding and mutation?
Ans: 
- Rebinding: a name is pointed to a new object.  
  Example: x = [1,2]; x = [3,4] → x points to a new list.  
- Mutation: the object itself changes.  
  Example: x = [1,2]; x.append(3) → list becomes [1,2,3].  
Mutation affects all names pointing to the same object.

# Rebinding vs Mutation
x = [1, 2]
y = x
x = [3, 4]   # rebinding: x now new list
print("y after rebinding:", y)

z = [1, 2]
w = z
z.append(3)  # mutation: z and w both see change
print("w after mutation:", w)
'''

# Multiple targets + mutation
a = b = [1]
a.append(2)
print("Value of b:", b)   # b also changed
