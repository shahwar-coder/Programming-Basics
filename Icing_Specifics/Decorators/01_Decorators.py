# ============================================================
# Decorators in Python — explained using a LOGIN example
# ============================================================

# PROBLEM:
# We want to restrict access to some pages.
# Only logged-in users should access them.
# Without decorators → repeated login checks everywhere.

# ============================================================
# 1. WITHOUT DECORATORS (repetition problem)
# ============================================================

def homepage(name, login_status):
    return "Home Page"

def products(name, login_status):
    return "Products Page"

def orders(name, login_status):
    if not login_status:
        return "Please login to access this page"
    return "Orders Page"

def profile(name, login_status):
    if not login_status:
        return "Please login to access this page"
    return "Profile Page"

print(homepage("Rahul Gandhi", True))
print(products("Rahul Gandhi", True))
print(orders("Rahul Gandhi", False))
print(profile("Rahul Gandhi", False))

# ❌ Issues:
# - Same login check repeated
# - Hard to maintain
# - Logic mixed with business code


# ============================================================
# 2. DECORATORS SOLVE THIS CLEANLY
# ============================================================

# A decorator WRAPS a function
# and adds behavior BEFORE calling it

def login_required(func):
    def wrapper(name, login_status):
        if login_status:
            return func(name, login_status)
        else:
            return "Please login to access this page"
    return wrapper

# ------------------------------------------------------------
# 3. Normal functions (NO login logic inside)
def homepage(name, login_status):
    return "Home Page"

def products(name, login_status):
    return "Products Page"

# ------------------------------------------------------------
# 4. Protected routes using decorator
@login_required
def orders(name, login_status):
    return "Orders Page"

@login_required
def profile(name, login_status):
    return "Profile Page"

# ------------------------------------------------------------
# 5. Function calls
print(homepage("Rahul Gandhi", True))
print(products("Rahul Gandhi", True))
print(orders("Rahul Gandhi", False))
print(profile("Rahul Gandhi", False))

# OUTPUT:
# Home Page
# Products Page
# Please login to access this page
# Please login to access this page


# ============================================================
# 6. What @login_required REALLY means
# ============================================================

# This line:
# @login_required
# def orders(...):

# Is equivalent to:
# orders = login_required(orders)


# ============================================================
# 7. Important nuance: use *args, **kwargs (scalable)
# ============================================================

def login_required(func):
    def wrapper(*args, **kwargs):
        name, login_status = args
        if login_status:
            return func(*args, **kwargs)
        return "Please login to access this page"
    return wrapper


# ============================================================
# 8. Preserve function metadata (best practice)
# ============================================================

from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name, login_status = args
        if login_status:
            return func(*args, **kwargs)
        return "Please login to access this page"
    return wrapper


# ============================================================
# 9. Why decorators are powerful (real-world)
# ============================================================

# ✔ Authentication / Authorization
# ✔ Logging
# ✔ Caching
# ✔ Rate limiting
# ✔ Validation
# ✔ Timing / Monitoring


# ============================================================
# 10. Mental model (KEY TAKEAWAY)
# ============================================================

# Decorator asks:
# "Should this function run?"
# "What extra rules apply before or after it?"

# Business logic stays CLEAN
# Cross-cutting concerns stay REUSABLE
