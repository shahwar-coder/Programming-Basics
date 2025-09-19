'''
Q. How to handle optional dependencies safely?
Ans: Use conditional imports with try/except to support optional features.

Example:
'''
try:
    import numpy as np
except ImportError:
    np = None

# Step-by-step:
# 1. Try importing numpy.
# 2. If not installed, np = None, program won’t crash.
