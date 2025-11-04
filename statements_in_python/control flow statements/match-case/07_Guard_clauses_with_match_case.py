'''
Q1. What are guard clauses in Python’s match/case?
Ans:
Guard clauses let you add an *extra condition* to a pattern.  
A case runs only if both the pattern matches **and** the condition is True.
'''
# Example
x = 7
match x:
    case n if n > 0:
        print("Positive")
    case n if n < 0:
        print("Negative")
    case _:
        print("Zero")


# Example
match num:
    case n if n % 2 == 0:
        print("Even")
    case n if n % 2 != 0:
        print("Odd")



'''
Q2. How does the guard clause work internally?
Ans:
1️⃣ First, Python checks if the pattern matches.  
2️⃣ Then, it evaluates the `if` condition.  
3️⃣ If both are true, that case runs; otherwise, it tries the next one.
'''



'''
Q3. What can guard clauses be used with?
Ans:
They work with *any pattern type* —  
literals, sequences, tuples, classes, or even nested patterns.
'''
# Example
match [1, 2, 3]:
    case [a, b, c] if sum([a, b, c]) > 5:
        print("Sum > 5")   # True → prints



'''
Q4. What happens if the guard condition fails?
Ans:
If the pattern matches but the guard condition fails,  
Python skips that case and continues checking the next one.
'''
# Example
x = 0
match x:
    case n if n > 0:
        print("Positive")
    case n if n == 0:
        print("Zero")      # Guard passes here



'''
Q5. What’s the key rule for guard clause evaluation order?
Ans:
Pattern first, condition second — always in that order.  
The condition won’t even run if the pattern doesn’t match.
'''
# Example
match ("ok", 10):
    case ("ok", n) if n > 5:
        print("Good value")   # matches + condition True
    case _:
        print("Fallback")
