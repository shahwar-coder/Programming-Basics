# Example 8: Using join() with generator expression
print(", ".join(word.upper() for word in ["python", "rocks"]))
# "PYTHON, ROCKS"
