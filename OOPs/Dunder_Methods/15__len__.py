'''
__len__ : tells python, when some someone askes about my length, return this number
'''

class Basket:
    def __init__(self, apples):
        self.apples = apples

    def __len__(self):
        return len(self.apples)

b = Basket(["🍎", "🍎", "🍎"])
print(len(b))

# 3
