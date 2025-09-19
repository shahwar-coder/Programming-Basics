'''
Q. Loop `else` — what is that? (very useful pattern)
Ans:
- `else` after a `for` or `while` runs **only if the loop completed normally** (no `break`).
- Useful for “search” patterns to avoid flags.
'''
# Problem (flag approach):
found = False
for x in items:
    if is_target(x):
        print("Found")
        found = True
        break
if not found:
    print("Not found")

# ===================================

# Better: loop-else
for x in items:
    if is_target(x):
        print("Found")
        break
else:
    print("Not found")

# Step-by-step (loop-else version):
# 1. Iterate items; on target -> print and break (else skipped).
# 2. If loop finishes without break -> else runs -> print "Not found".
