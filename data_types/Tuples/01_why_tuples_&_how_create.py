'''
Q1. Why do tuples exist in Python?
Ans. Tuples exist to store data that should NOT change. They are fixed-size and immutable.
'''
# Example
coords = (10, 20)
# Coordinates should not change → tuple is perfect


'''
Q2. What does “immutable” mean for tuples?
Ans. Immutable means once a tuple is created, its values cannot be changed.
'''
# Example
t = (1, 2, 3)
# t[0] = 99  ❌ Error (tuples cannot be modified)


'''
Q3. Why are tuples considered safer than lists?
Ans. Because their values cannot be changed accidentally, so bugs are reduced.
'''
# Example
def process_config(config):
    # config cannot be modified if it's a tuple
    pass

config = ("localhost", 8080)


'''
Q4. Why are tuples faster than lists?
Ans. Tuples are simpler internally (no resizing), so Python can access them faster.
'''
# Example
# Lists allow append/remove → more overhead
# Tuples are fixed → faster access


'''
Q5. What does “hashable” mean and why does it matter?
Ans. Hashable means a value can be used as a key in dictionaries or in sets.
'''
# Example
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai"
}
# Tuples work as keys, lists do NOT


'''
Q6. How do tuples express intent?
Ans. Using a tuple tells other developers: “This data should not change.”
'''
# Example
RGB_COLOR = (255, 0, 0)
# Color values are constants → tuple shows intent clearly


'''
Q7. How can you create a tuple in Python?
Ans. You can create tuples using parentheses OR just commas.
'''
# Examples
t1 = (1, 2, 3)
t2 = 1, 2, 3
# Both are tuples


'''
Q8. Why does a single-element tuple need a comma?
Ans. Without the comma, Python treats it as a normal value, not a tuple.
'''
# Example
x = (5)     # ❌ int, not tuple
y = (5,)    # ✅ tuple with one element
