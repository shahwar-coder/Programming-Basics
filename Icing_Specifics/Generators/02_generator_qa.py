'''
Q1. What is a generator in Python in simple terms?
A.
A generator is a function or expression that produces values one at a time,
only when asked, instead of storing all values in memory at once.
'''
# Example:
# def gen():
#     yield 1
#     yield 2
# g = gen()
# next(g)  # 1
# next(g)  # 2


'''
Q2. What problem do generators solve in backend systems?
A.
Generators solve the memory problem by allowing programs to process large data
(like files or streams) incrementally instead of loading everything at once.
'''
# Example:
# Reading a large CSV file row by row using yield
# instead of loading all rows into a list


'''
Q3. How is yield different from return?
A.
return ends the function permanently,
while yield pauses the function, remembers its state, and resumes later.
'''
# Example:
# def f():
#     yield 1
#     yield 2
# # Function continues after each yield


'''
Q4. What is the key difference between a generator and a list?
A.
A list stores all values in memory immediately,
whereas a generator computes values lazily, one at a time.
'''
# Example:
# [x for x in range(1000000)]   # high memory usage
# (x for x in range(1000000))   # constant memory


'''
Q5. Why are generators called iterators?
A.
Because they support iteration using next() and for-loops,
and they produce values sequentially until exhausted.
'''
# Example:
# gen = (x for x in range(3))
# for v in gen:
#     print(v)


'''
Q6. What is an important limitation of generators?
A.
Once a generator is exhausted, it cannot be reused and must be recreated.
'''
# Example:
# gen = (x for x in range(2))
# list(gen)  # [0, 1]
# list(gen)  # []  (already exhausted)
