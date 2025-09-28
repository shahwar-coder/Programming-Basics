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


# {'Running': 90000, 'Cycling': 62500, 'Swimming': 75625, 'Yoga': 14400, 'Jump Rope': 122500}
