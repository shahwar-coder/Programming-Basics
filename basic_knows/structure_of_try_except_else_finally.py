'''
Q. What is the structure of try/except/else/finally blocks?
Ans:
Structure:
try → code that might fail  
except → handles specific errors  
else → runs if no error occurs  
finally → always runs (cleanup or closing actions)
'''
# Example
try:
    x = int("10")
except ValueError:
    print("Error!")
else:
    print("Success!")
finally:
    print("Done")
# Output: Success! \n Done



'''
Q. What’s the order of execution when all blocks are present?
Ans:
try → (error?) → except (if any) → else (if no error) → finally (always).
'''
# Example
try:
    print("Try")
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")
# Output: Try → Else → Finally
