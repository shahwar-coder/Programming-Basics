# seed(x)

import random
random.seed(10)
print("seed(10) -> random():", random.random())
# → Output: same value on every run with same seed
# Sets the starting point for random numbers

# NOTES:
'''
Python’s random module does not generate truly random numbers.
It generates pseudo-random numbers using a mathematical formula (algorithm).

That algorithm needs a starting value → this starting value is called a seed.
'''
random.seed(10)
# ✔ Sets the starting point of the random number generator to 10.
# Think of it like this:
# Seed = starting position
# Random numbers = path taken from that position
# If the starting position is the same, the path will be the same.
