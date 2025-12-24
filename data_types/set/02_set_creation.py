'''
Q1. How do you create a set using curly braces?
Ans. Use curly braces with comma-separated values.
'''
# Example
s = {1, 2, 3}
# Creates a set with three unique elements


'''
Q2. What happens if you put duplicate values inside `{}`?
Ans. Python automatically removes duplicates.
'''
# Example
s = {1, 2, 2, 3}
# s becomes {1, 2, 3}


'''
Q3. How do you create a set from another iterable?
Ans. Use the `set()` constructor with an iterable.
'''
# Example
s = set([1, 2, 2, 3])
# s = {1, 2, 3}

s2 = set("hello")
# s2 = {'h', 'e', 'l', 'o'}


'''
Q4. What types of iterables can be passed to `set()`?
Ans. Any iterable like list, tuple, string, or range.
'''
# Example
set((1, 2, 3))
set(range(5))


'''
Q5. How do you create an empty set?
Ans. Use `set()`, not `{}`.
'''
# Example
empty = set()   # ✅ empty set
# {}            # ❌ empty dictionary


'''
Q6. Why does `{}` not create an empty set?
Ans. Because `{}` is reserved syntax for creating an empty dictionary.
'''
# Example
type({})        # dict
type(set())     # set


'''
Q7. When should you use `set(iterable)` instead of `{}`?
Ans. When you want to remove duplicates or convert data into a set.
'''
# Example
unique_names = set(names_list)


'''
Q8. What is the one-line rule to remember?
Ans. Use `{}` for non-empty sets and `set()` for empty sets or conversions.
'''
# Example (lock it 🔒)
# Empty set → set()
# Non-empty set → {a, b, c}
