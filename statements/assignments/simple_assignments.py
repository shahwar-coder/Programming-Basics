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
