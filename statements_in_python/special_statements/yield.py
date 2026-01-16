# ============================================================
# yield in Python — the REAL mental model (backend-friendly)
# ============================================================

# yield is NOT "return with a pause".
# yield is:
# - produce a value
# - freeze function state
# - resume exactly from here later

# If a function contains `yield`, it becomes a GENERATOR FUNCTION.


# ============================================================
# 1. yield vs return (MOST IMPORTANT)
# ============================================================

def with_return():
    return 1
    return 2   # never reached

def with_yield():
    yield 1
    yield 2    # both values are produced

# return → exits function forever
# yield  → pauses and remembers state


# ============================================================
# 2. What happens when function with yield is CALLED
# ============================================================

gen = with_yield()

# Function body does NOT run immediately
# It returns a generator object

print(gen)  # <generator object ...>


# ============================================================
# 3. What happens when next() is called
# ============================================================

print(next(gen))  # runs until first yield → 1
print(next(gen))  # resumes → 2
# next(gen) → StopIteration


# ============================================================
# 4. yield freezes EVERYTHING (state preservation)
# ============================================================

def counter():
    i = 0
    while True:
        yield i
        i += 1

gen = counter()
next(gen)  # 0
next(gen)  # 1
next(gen)  # 2

# Variables, loop position, stack — ALL remembered


# ============================================================
# 5. yield inside loops (COMMON BACKEND PATTERN)
# ============================================================

def stream_users(users):
    for user in users:
        if user["active"]:
            yield user   # stream one user at a time

# No list created → memory efficient


# ============================================================
# 6. yield turns function into ITERATOR
# ============================================================

gen = stream_users([
    {"name": "A", "active": True},
    {"name": "B", "active": False},
])

for user in gen:
    print(user)

# Generator supports:
# - for-loop
# - next()
# - lazy evaluation


# ============================================================
# 7. yield vs list comprehension
# ============================================================

# List comprehension → eager
active_users_list = [u for u in users if u["active"]]

# Generator expression → lazy
active_users_gen = (u for u in users if u["active"])


# ============================================================
# 8. yield + send() (ADVANCED, but important)
# ============================================================

def controlled_counter():
    i = 0
    while True:
        increment = yield i   # receives value from send()
        if increment is None:
            increment = 1
        i += increment

gen = controlled_counter()
next(gen)       # start generator
gen.send(5)     # jump by 5
gen.send(2)     # jump by 2


# ============================================================
# 9. yield + return (FINAL VALUE)
# ============================================================

def accumulate(nums):
    total = 0
    for n in nums:
        total += n
        yield total
    return total   # available via StopIteration.value

gen = accumulate([1, 2, 3])
try:
    for _ in gen:
        pass
except StopIteration as e:
    print(e.value)


# ============================================================
# 10. Backend-real examples of yield
# ============================================================

# ✔ Streaming CSV rows
# ✔ Streaming logs
# ✔ Processing API pagination
# ✔ ETL pipelines
# ✔ Infinite streams (events)


# ============================================================
# 11. Common mistakes
# ============================================================

# ❌ Expecting function to execute immediately
# ❌ Converting generator to list accidentally
# ❌ Reusing exhausted generator
# ❌ Mixing yield and return incorrectly


# ============================================================
# 12. Mental model (BURN THIS IN)
# ============================================================

# return:
# "I am DONE. Here is the result."

# yield:
# "Here is ONE value.
#  Come back later if you want more."
