'''
✅ Placeholder vs Pass
You’ve learned that both pass and ... can be used as placeholders in functions.

def a():
    pass

def b():
    ...

print(a())
print(b())

What will this print?
How is pass different from ... in behavior, if at all?
'''

def a():
    pass

def b():
    return ...

print(a()) # None
print(b()) # None

print(type(a())) # None
print(type(b())) # None

# The difference is :

'''
- pass is a keyword
- pass is a statement
- ellipsis is not a keyword
- ellipsis is an object

- pass has not meaning, does nothing
- ellipsis can have a semantic meaning, eg. in cases of numpy arrays slicing

- pass cannot be returned
- ellipsis can be returned
- examples:

```
def a():
    return pass # WRONG SYNTAX (cannot be returned)
```

```
def b():
    return ... # CORRECT SYNTAX (can be returned)
```
- Returns an Ellpsis Object : <class 'ellipsis'>
'''
