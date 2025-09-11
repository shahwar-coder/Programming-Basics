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

