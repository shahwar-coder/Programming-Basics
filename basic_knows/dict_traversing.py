'''
1️⃣ Dictionaries store data as key-value pairs:
    - "a": 1
    - "b": 2

2️⃣ d.items() gives you a sequence of (key, value) pairs:
    - It's like: [("a", 1), ("b", 2)]

3️⃣ for key, val in d.items():
    - Loops over each pair.
    - First loop: key = "a", val = 1
    - Second loop: key = "b", val = 2

4️⃣ You can now use key and value separately inside the loop.
'''

# This is traversing a dictionary
# Also manipulating values using dictionary comprehension
calories_burned = {
    "Running": 300,
    "Cycling": 250,
    "Swimming": 275,
    "Yoga": 120,
    "Jump Rope": 350
}

doubled_calories_burned = {k: v**2 for k,v in calories_burned.items()}
print(doubled_calories_burned)



