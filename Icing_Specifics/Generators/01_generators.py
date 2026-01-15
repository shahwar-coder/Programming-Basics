# ============================================================
# Generators in Python — Backend & Systems Perspective
# ============================================================

# CORE IDEA:
# A generator produces values ONE AT A TIME, on demand.
# It does NOT store all values in memory like a list.

# Think:
# list  → "give me everything now"
# gen   → "give me next when I ask"

# ============================================================
# 1. Why Generators exist (BACKEND REASON)
# ============================================================

# Backend systems deal with:
# - large files (CSV, logs)
# - streams (requests, events)
# - pipelines (ETL)

# Loading everything into memory = ❌
# Streaming data = ✅

# ============================================================
# 2. Generator function (yield)
# ============================================================

def count_up_to(n):
    i = 1
    while i <= n:
        yield i      # pause here, return value
        i += 1       # resume from here next time

gen = count_up_to(3)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) → StopIteration


# ============================================================
# 3. How yield REALLY works (important mental model)
# ============================================================

# yield:
# - returns a value
# - freezes function state
# - resumes from same line on next call

# NOT like return (which exits forever)


# ============================================================
# 4. Generator vs list (CRITICAL difference)
# ============================================================

def list_version(n):
    return [i for i in range(1, n + 1)]

def generator_version(n):
    for i in range(1, n + 1):
        yield i

# list_version(10_000_000)   ❌ huge memory
# generator_version(...)     ✅ constant memory


# ============================================================
# 5. Generator expressions (like list comprehension)
# ============================================================

nums = (x * 2 for x in range(5))

for n in nums:
    print(n)

# () → generator
# [] → list


# ============================================================
# 6. Generators are ITERATORS
# ============================================================

gen = count_up_to(3)

for value in gen:
    print(value)

# Once exhausted → cannot reuse
# Need to recreate generator


# ============================================================
# 7. Backend-real example: streaming CSV rows
# ============================================================

import csv

def read_users(path):
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row   # stream rows one by one

# Usage:
for user in read_users("users.csv"):
    validate(user)
    save_to_db(user)


# ============================================================
# 8. Generator pipelines (POWERFUL PATTERN)
# ============================================================

def filter_active(users):
    for user in users:
        if user["active"]:
            yield user

def extract_emails(users):
    for user in users:
        yield user["email"]

emails = extract_emails(
    filter_active(
        read_users("users.csv")
    )
)

# Memory-efficient ETL pipeline


# ============================================================
# 9. Common mistakes
# ============================================================

# ❌ Converting generator to list accidentally
# list(gen)  → destroys memory benefit

# ❌ Reusing exhausted generator
# for x in gen: ...
# for x in gen: ...  # nothing happens


# ============================================================
# 10. When to use generators (RULE OF THUMB)
# ============================================================

# ✔ Large data
# ✔ Streaming
# ✔ Pipelines
# ✔ Infinite sequences
# ❌ Small fixed data
# ❌ When random access is needed


# ============================================================
# 11. Mental Model (MOST IMPORTANT)
# ============================================================

# Generator asks:
# "What is the NEXT value?"

# List asks:
# "What are ALL the values?"
