'''
Q1. How does match/case actually work under the hood?
Ans:
- Evaluates the subject once.  
- Checks each case pattern from top to bottom.  
- Executes the *first* match found.  
- Then stops — no fall-through like in other languages.
'''
# Example
color = "red"
match color:
    case "red": print("Stop!")    # Only this runs
    case "yellow": print("Wait")
    case "green": print("Go")



'''
Q2. What are literal patterns in match/case?
Ans:
Literal patterns match exact values — similar to using `==`.  
They’re used for fixed comparisons like strings, numbers, or constants.
'''
# Example
day = "Mon"
match day:
    case "Mon": print("Week starts")     # exact match
    case "Sun": print("Weekend!")



'''
Q3. What is the wildcard pattern `_` and why is it useful?
Ans:
`_` means “match anything” — it’s the default or catch-all case.  
It’s like an “else” in if/else statements.
'''
# Example
cmd = "unknown"
match cmd:
    case "start": print("Begin")
    case "stop": print("End")
    case _: print("Unknown command")     # fallback



'''
Q4. How is match/case different from if/elif chains?
Ans:
- match/case is declarative — focuses on what pattern matches.  
- if/elif is procedural — checks each condition logically.  
match/case is cleaner for matching fixed values or structures.
'''
# Example
# if/elif version:
# if cmd == "start": ...
# elif cmd == "stop": ...
# else: ...

# match/case version:
match cmd:
    case "start": print("Go")
    case "stop": print("Halt")
    case _: print("Unknown")



'''
Q5. Why does Python’s match/case have no “fall-through”?
Ans:
To avoid bugs and make control flow predictable.  
Each case runs in isolation — once matched, the rest are ignored.
'''
# Example
num = 2
match num:
    case 1: print("One")
    case 2: print("Two")   # stops here
    case 3: print("Three") # never checked
