'''
📌 Lexical Structure Relevant to Statements

1. Indentation
• Defines code blocks (suites) in Python
• Consistent spacing required (PEP 8 → 4 spaces recommended)
• Mixing tabs + spaces → IndentationError

2. Whitespace
• Inside lines, spaces mostly cosmetic (x=1+2 vs x = 1 + 2)
• Leading spaces (indentation) are meaningful
• In type hints: x: int = 3  (spaces optional but style matters)

3. Line Breaks
• Normally: 1 statement = 1 logical line
• Explicit line joining → use "\" outside brackets
• Implicit line joining → allowed inside (), [], {}
  → Example:
     total = (1 +
              2 +
              3)

4. Semicolons (;)
• Can put multiple simple statements on one line
  Example: x = 1; y = 2; print(x + y)
• Legal but discouraged for readability

📝 Key Learnings from Q&A
• "x = 1 + ↩ 2 + 3" → ❌ Error (needs "\")
• "y = (1 + ↩ 2 + 3)" → ✅ Works (implicit joining)
• You correctly identified when "\" is required
'''


'''
Q1. Why is indentation important in Python, and what error occurs if you mix tabs and spaces?
Ans: Indentation defines code blocks (suites). Python enforces consistent 
indentation because it does not use braces {}. 
Mixing tabs and spaces causes an IndentationError.

Q2. Are spaces inside a statement meaningful in Python?
Ans: Mostly no. For example, x=1+2 and x = 1 + 2 are equivalent.  
But leading spaces (indentation) are meaningful, and style guides 
like PEP 8 recommend spaces for readability.

Q3. What is the difference between explicit and implicit line joining?
Ans: 
- Explicit line joining uses "\" to continue a statement to the next line.  
- Implicit line joining happens automatically inside (), [], {}.  
Example: 
    total = (1 + 
             2 + 
             3)   # works without "\"

Q4. Can semicolons be used in Python statements? 
Ans: Yes. Multiple simple statements can be placed on the same line 
using semicolons (;). Example: x=1; y=2; print(x+y)  
However, it is discouraged for readability.

Q5. (Coding)
# Explicit line joining
a = 1 + 2 + \
    3 + 4
print("Explicit join:", a)

# Implicit line joining inside ()
b = (1 + 2 +
     3 + 4)
print("Implicit join:", b)

# Multiple simple statements in one line (with ;)
x=10; y=20; print("Semicolons:", x+y)
'''
