from itertools import permutations

data = ['A', 'B', 'C']
result = permutations(data, 2)

for p in result:
    print(p)


# OUTPUT:
# ('A', 'B')
# ('A', 'C')
# ('B', 'A')
# ('B', 'C')
# ('C', 'A')
# ('C', 'B')

# REPETITIONS ALLOWED (unlike combinations)
