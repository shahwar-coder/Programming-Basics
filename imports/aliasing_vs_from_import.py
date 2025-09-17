# Compare directly:
import math as m
from math import sqrt

print(m.sqrt is math.sqrt)    # ✅ True (alias points to same module)
print(sqrt is math.sqrt)      # ✅ True (from-imported name is same object)
