'''
Q1. What does `yield` do in Python, in simple terms?
A.
`yield` produces a value and pauses the function.
The function remembers its state and resumes from the same place next time.
'''
# Example:
# def gen():
#     yield 1
#     yield 2
#
# g = gen()
# next(g)  # 1
# next(g)  # 2


'''
Q2. How is `yield` different from `return`?
A.
`return` ends the function forever.
`yield` pauses the function and allows it to continue later.
'''
# Example:
# def f1():
#     return 1
#     return 2   # never runs
#
# def f2():
#     yield 1
#     yield 2    # both values are produced


'''
Q3. What happens when a function with `yield` is called?
A.
The function does NOT run immediately.
It returns a generator object that can be iterated later.
'''
# Example:
# def gen():
#     yield 10
#
# g = gen()
# print(g)  # <generator object ...>


'''
Q4. How does `next()` work with a generator?
A.
`next()` runs the generator until the next `yield`,
returns that value, and pauses execution again.
'''
# Example:
# def gen():
#     yield "A"
#     yield "B"
#
# g = gen()
# next(g)  # "A"
# next(g)  # "B"


'''
Q5. What does it mean that `yield` preserves state?
A.
All local variables, loop positions, and execution context
are remembered between yields.
'''
# Example:
# def counter():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
# g = counter()
# next(g)  # 0
# next(g)  # 1
# next(g)  # 2


'''
Q6. Why is `yield` useful in backend systems?
A.
Because it allows processing large or infinite data
one item at a time without loading everything into memory.
'''
# Example:
# def stream_users(users):
#     for user in users:
#         yield user
#
# for u in stream_users(big_user_list):
#     process(u)
