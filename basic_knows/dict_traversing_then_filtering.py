'''
Q. How can you filter items inside a dict comprehension?
Ans:
- Add an if-condition at the end to include only certain pairs.
'''

calories_burned = {
    "Running": 300,
    "Cycling": 250,
    "Swimming": 275,
    "Yoga": 120,
    "Jump Rope": 350
}

filtered_300 = {k: v for k,v in calories_burned.items() if v>=300}
print(filtered_300)
