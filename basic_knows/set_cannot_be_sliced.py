'''
Set cannnot be sliced
It will give error
'''

s = {10, 20, 30, 40, 50}
print(s[1:3])

# TypeError: 'set' object is not subscriptable



'''
The FIX:
-> Convert to List type, them slice
'''
myset = {10, 20, 30, 40, 50}
mylist = list(myset)
print(mylist[0])     # access first element
print(mylist[1:3])   # slice like a list
