'''
Q1. Why are lambda functions sometimes called “anonymous functions”?
A.
Lambda functions are called anonymous because they do not have a name.
They exist only where they are defined and are usually not reused.
'''
# Example:
# (lambda x: x * 2)(5)
# Output → 10


'''
Q2. What is the late-binding (closure) problem with lambda functions?
A.
Lambda functions capture variables by reference, not by value.
This means they use the variable’s value at execution time, not creation time.
'''
# Example:
# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)
#
# [f() for f in funcs]
# Output → [2, 2, 2]


'''
Q3. How do you fix the late-binding issue in lambda functions?
A.
You fix it by using default arguments, which bind the value at creation time.
'''
# Example:
# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i: i)
#
# [f() for f in funcs]
# Output → [0, 1, 2]


'''
Q4. Why are lambda functions bad for debugging?
A.
Because lambda functions have no name, stack traces only show <lambda>,
making errors harder to trace and understand.
'''
# Example:
# data = [1, 2, 3]
# result = map(lambda x: x / 0, data)
# Error traceback shows: <lambda>


'''
Q5. Why should lambda functions not be overused in production code?
A.
Overusing lambdas reduces readability and makes code harder to maintain.
Complex logic is clearer and safer when written using def.
'''
# Example:
# ❌ Hard to read
# map(lambda x: x*x if x % 2 == 0 else x+1, data)
#
# ✅ Better
# def transform(x):
#     return x*x if x % 2 == 0 else x+1


'''
Q6. How are lambda functions commonly used in ML, RAG, or data pipelines?
A.
Lambda functions are used for quick transformations such as sorting,
filtering, or feature extraction inside pipelines.
'''
# Example:
# embeddings.sort(key=lambda v: v["score"], reverse=True)
# Top-k retrieval in RAG uses lambdas this way


'''
Q7. Are lambda functions faster than normal functions?
A.
No. Lambda functions are not faster than def functions.
They exist for convenience and clarity, not performance.
'''
# Example:
# lambda x: x + 1
# def inc(x): return x + 1
# Performance difference is negligible


'''
Q8. What is the best mental rule for using lambda functions?
A.
If the function logic fits naturally in one short line and is used immediately,
use lambda. Otherwise, use def.
'''
# Example:
# key=lambda x: x[1]   # good use
# lambda x: complex_multi_step_logic(x)  # bad use
