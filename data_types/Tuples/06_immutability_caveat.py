'''
Good example, it shows the tuple immutability caveat very clearly.
'''

tup = (1, [7, 8], 3)

a = tup
print("a:", a)

tup[1].append(9)

b = tup
print("b:", b)

print("a == b:", a == b)
print("a is b:", a is b)

# Output:
# a: (1, [7, 8], 3)
# b: (1, [7, 8, 9], 3)
# a == b: True
# a is b: True

'''
Here a and b seem to hold different values but why a == b and a is b , giving True
- Key Idea:
-> a and b do NOT store values. They store references (addresses) to the same object.
-> So even though the printed output looks different at two moments in time, both names still point to the same tuple object.
'''

# Just to make understood concept solid:
# print 'a' again, after the main change operation is done.

tup = (1, [7, 8], 3)

a = tup
print("a:", a)

tup[1].append(9)

b = tup
print("b:", b)
print("a:", a) # <-------- HERE

print("a == b:", a == b)
print("a is b:", a is b)

a: (1, [7, 8], 3)
b: (1, [7, 8, 9], 3)
a: (1, [7, 8, 9], 3)
a == b: True
a is b: True

# Since a and b points to same object, they will dispaly same values as well.


