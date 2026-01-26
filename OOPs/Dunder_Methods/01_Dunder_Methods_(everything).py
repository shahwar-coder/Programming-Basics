# ============================================================
# Dunder Methods in Python — Backend & Systems Perspective
# ============================================================

# Dunder (double-underscore) methods define how
# your objects behave INSIDE Python itself.
#
# They are NOT "nice to have".
# They are CONTRACTS with the Python runtime.

# ============================================================
# 1. __init__ — object initialization
# ============================================================

class User:
    def __init__(self, id: int, name: str):
        # Runs immediately after object creation
        # Used to initialize VALID state
        self.id = id
        self.name = name

# Called automatically:
u = User(1, "Rahul")

# Backend rules:
# ✔ initialize fields
# ✔ validate invariants
# ❌ no DB calls
# ❌ no network calls


# ============================================================
# 2. __repr__ — developer-facing representation
# ============================================================

class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        # Must be unambiguous and debug-friendly
        return f"User(id={self.id}, name={self.name})"

print(User(1, "Rahul"))
# Used in logs, debugging, tracing


# ============================================================
# 3. __str__ — user-facing string
# ============================================================

class Product:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

# print(product) → friendly output
# repr(product)  → debug output


# ============================================================
# 4. __eq__ — equality (BUSINESS LOGIC)
# ============================================================

class User:
    def __init__(self, id: int, email: str):
        self.id = id
        self.email = email

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id

# Equality ≠ same memory
# Equality = same business identity


# ============================================================
# 5. __hash__ — hashing consistency (CRITICAL)
# ============================================================

class User:
    def __init__(self, id: int):
        self.id = id

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

# Required when objects are used in:
# ✔ sets
# ✔ dict keys
# ✔ caches


# ============================================================
# 6. __bool__ — truthiness
# ============================================================

class FeatureFlag:
    def __init__(self, enabled: bool):
        self.enabled = enabled

    def __bool__(self):
        return self.enabled

# Enables:
# if feature_flag:


# ============================================================
# 7. __len__ — size semantics
# ============================================================

class Cart:
    def __init__(self, items: list):
        self.items = items

    def __len__(self):
        return len(self.items)

# Enables:
# if cart:
# len(cart)


# ============================================================
# 8. __iter__ — iteration support
# ============================================================

class UserCollection:
    def __init__(self, users: list):
        self.users = users

    def __iter__(self):
        return iter(self.users)

# Enables:
# for user in users:


# ============================================================
# 9. __enter__ / __exit__ — context managers
# ============================================================

class DBSession:
    def __enter__(self):
        print("Open connection")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Close connection")

# Enables:
# with DBSession():


# ============================================================
# 10. __getitem__ — index & key access
# ============================================================

class Config:
    def __init__(self, data: dict):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

# Enables:
# config["db_host"]


# ============================================================
# 11. __call__ — callable objects
# ============================================================

class Validator:
    def __call__(self, value):
        return value > 0

is_positive = Validator()
is_positive(10)


# ============================================================
# 12. How dataclasses relate (IMPORTANT)
# ============================================================

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

# Auto-generates:
# ✔ __init__
# ✔ __repr__
# ✔ __eq__


# ============================================================
# 13. Backend cheat-sheet
# ============================================================

# __init__    → object validity
# __repr__    → logs & debugging
# __str__     → user output
# __eq__      → business equality
# __hash__    → caching & sets
# __bool__    → state checks
# __len__     → collection semantics
# __iter__    → pipelines
# __enter__   → resource management
# __getitem__ → config / mapping
# __call__    → validators / strategies


# ============================================================
# 14. Mental Model (KEY TAKEAWAY)
# ============================================================

# Dunder methods define:
# "How my object behaves when Python interacts with it"

# They are the bridge between:
# your domain logic
# and Python’s runtime behavior
