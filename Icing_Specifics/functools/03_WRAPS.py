# ============================================================
# functools.wraps — backend-focused, concise but deep
# ============================================================

from functools import wraps

# PROBLEM:
# When we write decorators, the original function's identity is LOST
# (name, docstring, annotations, etc.)

# ------------------------------------------------------------
# 1. Problem WITHOUT @wraps
# ------------------------------------------------------------

def login_required(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@login_required
def orders():
    """Return orders page"""
    pass

print(orders.__name__)   # ❌ 'wrapper'
print(orders.__doc__)    # ❌ None

# This BREAKS:
# - logging
# - debugging
# - documentation
# - frameworks (FastAPI, Flask, Django)
# - introspection & decorators stacking


# ------------------------------------------------------------
# 2. Solution WITH @wraps
# ------------------------------------------------------------

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@login_required
def orders():
    """Return orders page"""
    pass

print(orders.__name__)   # ✅ 'orders'
print(orders.__doc__)    # ✅ 'Return orders page'


# ------------------------------------------------------------
# 3. What @wraps ACTUALLY DOES
# ------------------------------------------------------------

# @wraps(func) copies metadata from `func` → `wrapper`
# Internally, it assigns:
# wrapper.__name__        = func.__name__
# wrapper.__doc__         = func.__doc__
# wrapper.__module__      = func.__module__
# wrapper.__annotations__ = func.__annotations__
# wrapper.__wrapped__     = func   (VERY IMPORTANT)

# ------------------------------------------------------------
# 4. Why __wrapped__ matters (advanced but real)
# ------------------------------------------------------------

# Frameworks and tools use __wrapped__ to:
# - unwrap decorators
# - apply dependency injection
# - generate API docs
# - preserve type hints

# Example (conceptual):
# inspect.signature(my_function) works correctly
# ONLY if @wraps is used


# ------------------------------------------------------------
# 5. Backend-real example (login_required)
# ------------------------------------------------------------

def login_required(func):
    @wraps(func)
    def wrapper(name, login_status):
        if not login_status:
            return "Please login"
        return func(name, login_status)
    return wrapper

@login_required
def profile(name, login_status):
    """Profile page"""
    return "Profile Page"

print(profile.__name__)  # profile (important for routing)
print(profile.__doc__)   # Profile page


# ------------------------------------------------------------
# 6. Multiple decorators (wraps is MANDATORY)
# ------------------------------------------------------------

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.4f}s")
        return result
    return wrapper

@logger
@timer
def fetch_orders():
    """Fetch orders from DB"""
    pass

print(fetch_orders.__name__)  # fetch_orders (not wrapper)


# ------------------------------------------------------------
# 7. When NOT using @wraps breaks things
# ------------------------------------------------------------

# ❌ API routing breaks
# ❌ Swagger/OpenAPI docs missing
# ❌ Decorators cannot be introspected
# ❌ Debugging stack traces confusing
# ❌ Type checking fails


# ------------------------------------------------------------
# 8. Golden rule (INDUSTRY STANDARD)
# ------------------------------------------------------------

# If you write a decorator that wraps a function:
# 👉 ALWAYS use @wraps(func)

# No exception.


# ------------------------------------------------------------
# 9. Mental model (KEY TAKEAWAY)
# ------------------------------------------------------------

# Decorator = new function
# @wraps = copy identity of old function to new one

# Think:
# wrapper "pretends" to be the original function
