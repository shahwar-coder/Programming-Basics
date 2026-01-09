'''
Q1. What does map() do in Python?
A.
map() applies a function to each element of an iterable
and returns the transformed results.
It answers: “Given x, what should x become?”
'''
# Example:
# numbers = [1, 2, 3]
# result = list(map(lambda x: x * 2, numbers))
# Output: [2, 4, 6]


'''
Q2. Why does map() return an iterator instead of a list?
A.
map() returns an iterator to save memory and support lazy evaluation.
Values are produced only when needed.
'''
# Example:
# result = map(lambda x: x + 1, [1, 2, 3])
# print(result)        # <map object>
# print(list(result))  # [2, 3, 4]


'''
Q3. How is map() different from filter()?
A.
map() transforms every element,
while filter() selects only elements that satisfy a condition.
'''
# Example:
# nums = [1, 2, 3, 4]
# mapped = list(map(lambda x: x * 2, nums))        # [2, 4, 6, 8]
# filtered = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]


'''
Q4. Can map() work with multiple iterables?
A.
Yes. map() applies the function element-wise across iterables.
Iteration stops at the shortest iterable.
'''
# Example:
# a = [1, 2, 3]
# b = [10, 20, 30]
# result = list(map(lambda x, y: x + y, a, b))
# Output: [11, 22, 33]


'''
Q5. When should map() be preferred over a for-loop?
A.
Use map() when the transformation is simple, short,
and you want a functional or pipeline-style approach.
'''
# Example:
# numbers = [1, 2, 3]
# doubled = list(map(lambda x: x * 2, numbers))
# Equivalent to a short for-loop


'''
Q6. map() vs list comprehension — which is better?
A.
Both do the same job.
List comprehensions are often more readable,
but map() is useful for functional pipelines and multiple iterables.
'''
# Example:
# map_version = list(map(lambda x: x * 2, [1, 2, 3]))
# lc_version  = [x * 2 for x in [1, 2, 3]]


# =|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|

'''
Q1. How is map() used in data preprocessing for ML?
A.
map() is used to transform raw data into a usable numerical form
before feeding it to an ML model.
This includes scaling, encoding, or feature extraction.
'''
# Example:
# raw = ["10", "20", "30"]
# features = list(map(lambda x: int(x), raw))
# Output: [10, 20, 30]


'''
Q2. How does map() help in feature engineering?
A.
map() applies the same feature transformation to all samples,
ensuring consistency across the dataset.
'''
# Example:
# heights_cm = [150, 160, 170]
# heights_m = list(map(lambda h: h / 100, heights_cm))
# Output: [1.5, 1.6, 1.7]


'''
Q3. How is map() used with embeddings in NLP or GenAI?
A.
map() can be used to transform text into embeddings
by applying an embedding function to each text item.
'''
# Example:
# texts = ["hello", "world"]
# embeddings = list(map(get_embedding, texts))
# Each element becomes a vector representation


'''
Q4. How does map() fit into functional pipelines (ETL / RAG)?
A.
map() is commonly chained with filter() to clean and transform data
step-by-step in retrieval and preprocessing pipelines.
'''
# Example:
# docs = ["AI", "", "ML"]
# processed = list(
#     map(lambda d: d.lower(), filter(lambda d: d != "", docs))
# )
# Output: ['ai', 'ml']


'''
Q5. Why is map() useful for batch processing in ML?
A.
map() allows the same operation to be applied to every item in a batch,
which matches how ML models expect uniform transformations.
'''
# Example:
# batch = [1.0, 2.0, 3.0]
# normalized = list(map(lambda x: x / max(batch), batch))
# Output: [0.333..., 0.666..., 1.0]


'''
Q6. How does map() conceptually relate to neural network layers?
A.
A neural network layer applies the same transformation to many inputs.
Conceptually, this is similar to map(): one rule applied to many items.
'''
# Example:
# inputs = [[1, 2], [3, 4]]
# outputs = list(map(lambda v: W @ v, inputs))
# Each input vector is transformed the same way

