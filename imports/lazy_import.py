'''
Q1. What is a lazy import, and why is it useful?
Ans: A lazy import delays loading a module until the code actually uses it.  
This saves startup time if the module is rarely needed.

Example:
'''
def load_data():
    import pandas as pd   # imported only when function is called
    print(pd.__version__)

# Step-by-step:
# 1. Defining load_data() does NOT import pandas.
# 2. Calling load_data() triggers the import.



'''
Q2. Why avoid heavy top-level imports?
Ans: Heavy libraries at top-level slow down program startup, even if unused.

Example:
'''
# Bad (always loads pandas, slows startup)
import pandas as pd

# Better: import inside __main__ or functions
if __name__ == "__main__":
    import pandas as pd
    print("Pandas loaded")
