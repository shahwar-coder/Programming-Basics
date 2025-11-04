'''
Q1. What are “or-patterns” in Python’s match/case?
Ans:
Or-patterns let you match *multiple possibilities* in one case.  
They work like an “or” between patterns.
'''
# Example
status = "working"
match status:
    case "running" | "working" | "processing":
        print("Active")    # runs because "working" matches
    case _:
        print("Inactive")



'''
Q2. What is the syntax for an or-pattern?
Ans:
Use the `|` symbol to combine patterns:
`case pattern1 | pattern2 | pattern3:`
It checks each one in order.
'''
# Example
signal = "green"
match signal:
    case "red" | "yellow" | "green":
        print("Valid signal!")



'''
Q3. What happens when one of the subpatterns matches?
Ans:
The case runs immediately for the *first matching* subpattern.  
Python does not test the others.
'''
# Example
mode = "auto"
match mode:
    case "manual" | "auto":
        print("Supported mode")   # stops here
    case _:
        print("Unknown mode")



'''
Q4. What’s the rule about variable binding in or-patterns?
Ans:
All subpatterns in an or-pattern must bind the *same variables*.  
You can’t mix patterns that introduce different variable names.
'''
# case (x, y) | (a, b) ❌ → ambiguous names
# case (x, y) | (x, z) ✅ → consistent variable set {x, ?}
# case (x, y) | (x, y) ✅ → identical names
# case (1, y) | (2, z) ❌ → inconsistent variable set {y} vs {z}



'''
Q5. Why are or-patterns useful?
Ans:
They make code cleaner and remove repetition.  
Instead of writing multiple cases for similar conditions,  
you can combine them into one expressive pattern.
'''
# Example
match file_type:
    case "jpg" | "png" | "gif":
        print("Image file")
    case "mp4" | "avi":
        print("Video file")
    case _:
        print("Unknown format")



'''
Q6. Do or-patterns still follow the “first match wins” rule?
Ans:
Yes! As soon as one pattern matches, Python stops checking others —  
same as normal match/case behavior.
'''
# Example
n = 5
match n:
    case 1 | 3 | 5 | 7 | 9:
        print("Odd")
    case 2 | 4 | 6 | 8:
        print("Even")
