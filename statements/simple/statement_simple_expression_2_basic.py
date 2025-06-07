'''
✅ Question 1: Understand Side Effects

def shout(word):
    print(word.upper())

words = ["hello", "world"]
for w in words:
    shout(w)

Question:
What kind of statement is shout(w) in the loop?
Explain why it's written that way even though the return value is ignored.
'''

# It is an expression statement
# There is nor return value, and there was never intension to use it, so having the print from the funcall is just a side effect.
# Hence, shout(w) is an expression statement, used to trigger useful side effect (eg, printing)
