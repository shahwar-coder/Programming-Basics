'''
Q1. Why are tuples good for fixed records?
Ans. Because tuples cannot change, they safely represent fixed data like records.
'''
# Example
student = (101, "Rahul", "Delhi")
# ID, Name, City → fixed structure, no accidental changes


'''
Q2. How are tuples useful for function return values?
Ans. Functions can return multiple values as a single tuple.
'''
# Example
def get_min_max(nums):
    return min(nums), max(nums)

result = get_min_max([3, 7, 1])
# result = (1, 7)


'''
Q3. Why can tuples be used as dictionary keys?
Ans. Because tuples are hashable (immutable), unlike lists.
'''
# Example
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai"
}
# Tuple keys work, list keys do NOT


'''
Q4. What is the role of tuples in `*args`?
Ans. `*args` collects multiple function arguments into a tuple.
'''
# Example
def add_all(*args):
    return sum(args)

add_all(1, 2, 3)
# args = (1, 2, 3)


'''
Q5. Why are tuples used to design safer APIs?
Ans. They prevent callers from accidentally modifying returned data.
'''
# Example
def get_config():
    return ("localhost", 8080)

config = get_config()
# config[0] = "127.0.0.1" ❌ not allowed


'''
Q6. Why are tuples preferred when data should not change?
Ans. They clearly express intent: “this data is read-only.”
'''
# Example
RGB = (255, 0, 0)
# Constant values → tuple shows intent


'''
Q7. How do tuples help reduce bugs?
Ans. Immutability prevents unintended side effects from data modification.
'''
# Example
# Passing tuple instead of list → safer function behavior


'''
Q8. What is the one-line rule to remember?
Ans. Use tuples for fixed, safe, read-only data and lists for changeable data.
'''
# Example (lock it 🔒)
# Fixed & safe → tuple
# Changeable → list
