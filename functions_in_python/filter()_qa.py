'''
Q1. What does filter() do in Python?
A.
filter() selects elements from an iterable for which a given function returns True.
It does not modify elements; it only decides whether to keep or discard them.
'''
# Example:
# numbers = [1, 2, 3, 4, 5]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# Output: [2, 4]


'''
Q2. What kind of function does filter() expect?
A.
filter() expects a function that takes one element
and returns either True or False.
Only elements returning True are kept.
'''
# Example:
# words = ["hi", "hello", "cat"]
# result = list(filter(lambda w: len(w) > 3, words))
# Output: ["hello"]


'''
Q3. What does filter() return and why is that important?
A.
filter() returns an iterator, not a list.
This allows lazy evaluation and saves memory, but you must convert it to a list
to see the values.
'''
# Example:
# nums = [-1, 0, 2, 4]
# f = filter(lambda x: x > 0, nums)
# print(list(f))
# Output: [2, 4]


'''
Q4. How does filter(None, iterable) work?
A.
When None is passed instead of a function,
filter() removes all falsy values such as 0, "", None, and False.
'''
# Example:
# values = [0, 1, "", "hi", None, 5]
# result = list(filter(None, values))
# Output: [1, "hi", 5]


'''
Q5. How is filter() different from map()?
A.
filter() selects elements based on a condition,
while map() transforms every element regardless of condition.
'''
# Example:
# nums = [1, 2, 3]
# mapped = list(map(lambda x: x * 2, nums))
# filtered = list(filter(lambda x: x % 2 == 0, nums))
# mapped   → [2, 4, 6]
# filtered → [2]


'''
Q6. When should you prefer list comprehension over filter()?
A.
List comprehensions are often more readable for simple conditions
and are preferred in most Python code unless a functional pipeline is needed.
'''
# Example:
# nums = [-2, -1, 0, 3]
# result = [x for x in nums if x > 0]
# Output: [3]


# =|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|

'''
Q1. How is filter() used in Machine Learning data preprocessing?
A.
In ML, filter() is used to remove unwanted or invalid data points
before training, such as null values, outliers, or irrelevant samples.
'''
# Example:
# dataset = [10, None, 25, None, 40]
# clean_data = list(filter(lambda x: x is not None, dataset))
# Output: [10, 25, 40]


'''
Q2. How does filter() help in feature selection?
A.
filter() can be used to keep only features that satisfy certain conditions,
such as minimum variance, valid ranges, or non-zero importance.
'''
# Example:
# features = [0.1, 0.0, 2.3, 0.0, 1.5]
# useful = list(filter(lambda f: f != 0.0, features))
# Output: [0.1, 2.3, 1.5]


'''
Q3. How is filter() useful in NLP pipelines?
A.
In NLP, filter() is commonly used to remove stopwords,
short tokens, or invalid text entries before vectorization.
'''
# Example:
# words = ["AI", "is", "fun", "to", "learn"]
# tokens = list(filter(lambda w: len(w) > 2, words))
# Output: ["fun", "learn"]


'''
Q4. How can filter() be used in recommendation systems?
A.
filter() helps remove items a user has already seen or interacted with,
so recommendations only include new or relevant items.
'''
# Example:
# all_items = ["A", "B", "C", "D"]
# seen_items = {"A", "C"}
# recommendations = list(filter(lambda i: i not in seen_items, all_items))
# Output: ["B", "D"]


'''
Q5. Why is filter() suitable for streaming or large-scale data?
A.
Because filter() returns an iterator, it processes data lazily,
making it memory-efficient for large datasets or streaming pipelines.
'''
# Example:
# stream = range(1_000_000)
# positives = filter(lambda x: x > 0, stream)
# Data is processed one element at a time, not all at once


'''
Q6. How does filter() fit into functional ML pipelines?
A.
filter() is often combined with map() to build clean,
step-by-step data transformation pipelines used in ML workflows.
'''
# Example:
# nums = [-3, -1, 2, 4]
# pipeline = list(
#     map(lambda x: x * 2, filter(lambda x: x > 0, nums))
# )
# Output: [4, 8]
