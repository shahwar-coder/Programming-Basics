'''
Q1. How are decorators used in real-world systems like web apps or APIs?
A.
Decorators are used to enforce cross-cutting rules such as authentication,
authorization, rate limiting, and logging without mixing them into business logic.
In AI systems, this keeps model code clean and reusable.
'''
# Example:
# @login_required
# def get_user_embeddings(user_id):
#     return embeddings[user_id]


'''
Q2. How can decorators help in logging and monitoring AI/ML pipelines?
A.
Decorators can automatically log function calls, execution time,
inputs, and outputs without changing model or data code.
This is crucial for debugging and monitoring ML pipelines.
'''
# Example:
# def log_execution(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_execution
# def train_model(data):
#     pass


'''
Q3. How are decorators used for caching in AI or RAG systems?
A.
Decorators can cache expensive computations such as embeddings,
LLM responses, or database queries to avoid recomputation.
This improves latency and reduces cost.
'''
# Example:
# from functools import lru_cache
#
# @lru_cache(maxsize=1000)
# def get_embedding(text):
#     return embedding_model.encode(text)


'''
Q4. How do decorators help with rate limiting in GenAI applications?
A.
Decorators can enforce limits on how often a function is called,
which is critical when using paid APIs like LLMs or vector databases.
'''
# Example:
# @rate_limit(calls=5, per_second=1)
# def generate_answer(prompt):
#     return llm(prompt)


'''
Q5. How can decorators be used for validation in ML workflows?
A.
Decorators can validate inputs (shape, type, range)
before a model runs, preventing silent bugs and bad predictions.
'''
# Example:
# def validate_input(func):
#     def wrapper(x):
#         assert len(x) == 768
#         return func(x)
#     return wrapper
#
# @validate_input
# def predict(embedding):
#     pass


'''
Q6. Why are decorators important for clean AI system design?
A.
Decorators separate concerns:
- core logic (model, embeddings, inference)
- system rules (logging, auth, caching)
This leads to modular, testable, and maintainable AI systems.
'''
# Example:
# @log_execution
# @cache_result
# @validate_input
# def semantic_search(query_embedding):
#     pass
