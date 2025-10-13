from itertools import combinations
word = "HOUSE"
for combination in combinations(word, 3):
    print(combination)

# OUTPUT:
# ('H', 'O', 'U')
# ('H', 'O', 'S')
# ('H', 'O', 'E')
# ('H', 'U', 'S')
# ('H', 'U', 'E')
# ('H', 'S', 'E')
# ('O', 'U', 'S')
# ('O', 'U', 'E')
# ('O', 'S', 'E')
# ('U', 'S', 'E')
