'''
Q1. What is the purpose of the match/case statement in Python?
Ans:
It’s used for *pattern matching* — checking a value or structure 
against multiple patterns and running code for the first match.
It makes long if/elif chains simpler and cleaner.
'''
# Example
command = "start"
match command:
    case "start":
        print("Engine on")
    case "stop":
        print("Engine off")



'''
Q2. When was match/case introduced and why?
Ans:
Introduced in **Python 3.10**, it provides *structural pattern matching*.  
It’s more powerful than switch/case in other languages — 
because it can match not only values but also data shapes.
'''
# Example
point = (4, 5)
match point:
    case (x, y):
        print("2D point")    # matches structure of two items



'''
Q3. How is match/case better than long if/elif chains?
Ans:
It’s cleaner, more readable, and shows intent clearly.  
Each pattern case is independent — no need for repetitive `if` checks.
'''
# Example
# Instead of:
# if cmd == "start": ...
# elif cmd == "stop": ...
# elif cmd == "pause": ...

# Use:
match cmd:
    case "start": print("Go")
    case "stop": print("Halt")
    case "pause": print("Wait")



'''
Q4. What kinds of things can match/case work with?
Ans:
It can match:
- Simple values (like strings or numbers)
- Data structures (tuples, lists, dicts)
- Object attributes
- Even types and patterns with variable unpacking
'''
# Example
data = [1, 2, 3]
match data:
    case [a, b, c]:
        print("List of 3 items:", a, b, c)



'''
Q5. When should we *prefer* if/elif instead of match/case?
Ans:
If your logic is about *conditions* or *comparisons* 
(e.g., `x > 5`, `x % 2 == 0`),  
then use if/elif — match/case works best for *pattern comparisons*.
'''
# Example
x = 7
if x > 5:
    print("Greater than 5")   # condition-based → use if/elif



'''
Q6. What does “structural” mean in structural pattern matching?
Ans:
It means Python looks at the *shape* or *structure* of the data —
like number of elements, keys, or attributes —
instead of just comparing plain values.
'''
# Example
point = (10, 20, 30)
match point:
    case (x, y): print("2D")
    case (x, y, z): print("3D")   # Matches because structure has 3 elements

