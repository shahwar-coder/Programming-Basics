'''
1. “Expression is something that produces a value”
✅ Correct — an expression always evaluates to a value.

2. “Statements are instructions”
✅ Correct — a statement tells Python to perform an action.

3. “Statements tell Python to do something, It can be Check conditions, Return a value, Assign a value etc.”
🟨 Almost perfect.
✔️ Yes, statements can check conditions (if), assign (=), return (return), etc.
➕ Missing: statements can also define (def, class), import modules, handle errors (try/except), manage resources (with), and more.

4. “Every statement might have an expression but every expression might not be an statement.”
🟨 Slightly off in wording.
✔️ Correct idea: many statements contain expressions (e.g. if x > 0: contains expression x > 0).
❗ But not every statement has to include an expression (e.g. pass, break, continue don’t).

5. “One important thing to notice via an example is: 2+3 is different than x=2+3.”
✅ Perfect illustration.
✔️ 2+3 is just an expression.
✔️ x=2+3 is an assignment statement (that contains the expression 2+3).

Q1. Can every statement contain an expression?
Ans: No. Not every statement contains an expression.  
Examples: pass, continue, break are pure statements without expressions.

Q2. Why is `if x > 0:` considered a statement?
Ans: Because it is a control-flow instruction to Python (a statement).  
Inside it, the condition `x > 0` is an expression that evaluates to True/False.

Q3. What kinds of instructions are always statements?
Ans: Statements like def, class, import, with, try/except/finally are 
structural instructions. They cannot be reduced to just expressions.

Q4. (Coding)
# Expression only
2 + 3     # evaluates to 5

# Statement with expression
x = 2 + 3   # assignment statement, contains the expression 2+3

# Statement without expression
pass      # no expression inside
'''
