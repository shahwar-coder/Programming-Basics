'''
Q1. What is the purpose of `elif`?
Ans:
- Lets you test multiple conditions in sequence without nesting.
- Cleaner than writing `if` inside another `if`.
'''
# Problem (without elif, messy nesting):
x = 15
if x < 0:
    print("Negative")
else:
    if x == 0:
        print("Zero")
    else:
        if x < 10:
            print("Small positive")
        else:
            print("Large positive")

# Fix (with elif, cleaner):
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
elif x < 10:
    print("Small positive")
else:
    print("Large positive")



'''
Q2. How does order of conditions affect results?
Ans:
- Python checks top-to-bottom.
- The first True condition executes; the rest are skipped.

Example:
'''
x = 5
if x < 10:
    print("Less than 10")
elif x < 20:
    print("Less than 20")
# Step-by-step:
# 1. Check x < 10 -> True -> print "Less than 10"
# 2. Later elif skipped, even though it's also True.



'''
Q3. What happens if no condition matches?
Ans:
- The `else` block (if present) runs.
- If no `else`, nothing happens.

Example:
'''
x = -1
if x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("Other")

# Step-by-step:
# 1. x == 0 -> False
# 2. x == 1 -> False
# 3. else runs -> "Other"



'''
Q4. Why use elif instead of multiple if statements?
Ans:
- `elif` ensures only one branch runs.
- Multiple independent `if`s could trigger multiple blocks.
'''
# Problem (bad multiple ifs):
x = 0
if x >= 0:
    print("Non-negative")   # runs
if x == 0:
    print("Zero")           # also runs

# Fix (elif avoids double firing):
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Step-by-step:
# First True branch wins, others skipped.



'''
Q5. Pitfalls & Best Practices
Ans:
- Pitfall: Overlapping ranges can hide bugs (order matters).
- Pitfall: Too many elifs → long chain, maybe use dict-based dispatch or match-case.
- Best practice: Arrange conditions from most specific to most general.
'''


'''
Q6. Quick shorthand
- `if` → one condition
- `elif` → extra exclusive branches
- `else` → fallback
- Order matters: first match wins
'''
