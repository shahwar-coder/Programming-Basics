# Compare directly:
import math as m
from math import sqrt

print(m.sqrt is math.sqrt)    # ✅ True (alias points to same module)
print(sqrt is math.sqrt)      # ✅ True (from-imported name is same object)


'''
+--------------------------+-----------------------------+-------------------------------+
| Feature                  | import module as alias      | from module import name       |
+--------------------------+-----------------------------+-------------------------------+
| What it binds            | Whole module (as alias)     | Specific object(s) from module|
| Access style             | alias.attr                  | name directly                 |
| Example                  | import math as m            | from math import sqrt         |
| Usage                    | m.sqrt(16)                  | sqrt(16)                      |
| Namespace pollution      | Minimal (1 alias name)      | More (adds each imported name)|
| Risk of clashes          | Very low                    | Higher (names can overwrite)  |
| Best for                 | Large modules, clarity      | Few frequently used functions |
| Object identity          | alias is module object      | name is the exact same object |
+--------------------------+-----------------------------+-------------------------------+
'''
