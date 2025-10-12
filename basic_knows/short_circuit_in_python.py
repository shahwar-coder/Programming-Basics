'''
Q. What’s a common pitfall with or/and evaluation?
Ans:
- Short-circuiting: Python stops evaluating once the result is known.
  → and stops at first False, or stops at first True.
'''
def test(msg):
    print(msg)
    return True

# Short-circuit demo
print(False and test("Won’t print"))  # Stops before calling test()
print(True or test("Won’t print"))    # Stops before calling test()
