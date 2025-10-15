from itertools import combinations

data = ['A', 'B', 'C']
result = combinations(data, 2)

for c in result:
    print(c)


# OUTPUT:
# ('A', 'B')
# ('A', 'C')
# ('B', 'C')

# DOES NOT ALLOW REPETITION 
