'''
Q1. Why can tuples be used as dictionary keys?
Ans. Because tuples are hashable (immutable), unlike lists.
'''
# Example
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai"
}
# Tuple keys work, list keys do NOT
