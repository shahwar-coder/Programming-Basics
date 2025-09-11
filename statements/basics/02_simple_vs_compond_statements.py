'''
📌 Simple Statements
• Smallest unit of instruction (one logical line)
• Examples: pass, x = 5, return 3, break, continue
• Multiple simple statements can share one line using ;
'''
pass

'''
📌 Compound Statements
• Control or group other statements
• Structure = header (ends with :) + suite (indented block)
• Examples: if, for, while, try, with, def, class, match
'''

if x > 0:           # header
    print("positive")   # suite
else:
    print("not positive")

'''
Q1. What is the difference between a simple statement and a compound statement in Python?
Ans: 
- A simple statement is the smallest unit of instruction, usually written in one logical line.  
  Examples: pass, x=5, return 3, break, continue.  
- A compound statement controls or groups other statements.  
  It has a header (ending with :) and a suite (an indented block).  
  Examples: if, for, while, try, with, def, class, match.

Q2. Can multiple simple statements be written on a single line? If yes, how?
Ans: Yes. Multiple simple statements can be placed on the same line 
if separated by semicolons (;).  
Example: x=5; y=10; print(x+y)

Q3. Why must compound statements in Python use indentation?
Ans: Because the suite (block of code) in a compound statement 
must be clearly separated from the header.  
Python uses indentation instead of braces {} to define blocks.

Q4. (Coding)
# Simple statements (all in one line)
x = 10; y = 20; print(x+y)

# Compound statement (if with suite)
if x > y:
    print("x is greater")
else:
    print("y is greater")

'''
