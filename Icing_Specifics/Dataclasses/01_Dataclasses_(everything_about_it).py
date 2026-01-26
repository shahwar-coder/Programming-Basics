# ============================================================
# dataclasses in Python — Backend & Systems Perspective
# ============================================================

# dataclasses solve a VERY common backend problem:
# "I need a clean data container with minimal boilerplate"

# Instead of writing __init__, __repr__, __eq__ manually,
# Python generates them for you.

from dataclasses import dataclass, field, asdict
from typing import Optional, List
from datetime import datetime


# ============================================================
# 1. The problem dataclasses solve
# ============================================================

# WITHOUT dataclass (classic backend pain):
class UserOld:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"UserOld(id={self.id}, name={self.name}, email={self.email})"


# ============================================================
# 2. Basic dataclass (MOST COMMON USAGE)
# ============================================================

@dataclass
class User:
    id: int
    name: str
    email: str

u = User(1, "Rahul", "rahul@mail.com")

# Auto-generated:
# ✔ __init__
# ✔ __repr__
# ✔ __eq__
print(u)


# ============================================================
# 3. Why backend engineers LOVE dataclasses
# ============================================================

# ✔ Clean data models
# ✔ Strong typing
# ✔ Easy logging/debugging
# ✔ Easy conversion to dict / JSON
# ✔ Less boilerplate


# ============================================================
# 4. Default values & Optional fields
# ============================================================

@dataclass
class Product:
    id: int
    name: str
    price: float
    in_stock: bool = True
    description: Optional[str] = None

p = Product(1, "Laptop", 75000.0)


# ============================================================
# 5. field() — control behavior (VERY IMPORTANT)
# ============================================================

@dataclass
class Order:
    id: int
    items: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

# Why default_factory?
# ❌ items: List[str] = []   (BUG — shared across instances)
# ✅ default_factory=list   (safe)


# ============================================================
# 6. Immutable dataclasses (READ-ONLY MODELS)
# ============================================================

@dataclass(frozen=True)
class Token:
    value: str
    expires_at: datetime

t = Token("abc123", datetime.utcnow())
# t.value = "x"  ❌ raises FrozenInstanceError

# Useful for:
# ✔ config objects
# ✔ auth tokens
# ✔ value objects


# ============================================================
# 7. Custom logic with __post_init__
# ============================================================

@dataclass
class Employee:
    id: int
    name: str
    salary: float

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")

# Runs AFTER auto __init__


# ============================================================
# 8. Converting dataclass → dict / JSON
# ============================================================

user = User(1, "Rahul", "rahul@mail.com")

user_dict = asdict(user)
# {'id': 1, 'name': 'Rahul', 'email': 'rahul@mail.com'}

# Common backend pattern:
# json.dumps(asdict(user))


# ============================================================
# 9. Dataclass vs dict (IMPORTANT DISTINCTION)
# ============================================================

# dict:
# ✔ flexible
# ❌ no structure
# ❌ no type safety

# dataclass:
# ✔ structured
# ✔ typed
# ✔ self-documenting
# ✔ IDE & static checker friendly


# ============================================================
# 10. Dataclass vs Pydantic (BACKEND REALITY)
# ============================================================

# dataclass:
# ✔ standard library
# ✔ lightweight
# ❌ no runtime validation from external input

# pydantic:
# ✔ validation
# ✔ parsing
# ✔ API-ready
# ❌ heavier

# Rule of thumb:
# - Internal models → dataclass
# - API boundaries → pydantic


# ============================================================
# 11. Advanced options (know they exist)
# ============================================================

@dataclass(order=True)
class Score:
    value: int

# order=True → enables <, >, <= comparisons


@dataclass(slots=True)
class CompactUser:
    id: int
    name: str

# slots=True → lower memory, faster attribute access
# (great for large-scale backend systems)


# ============================================================
# 12. Real backend use cases
# ============================================================

# ✔ DTOs (Data Transfer Objects)
# ✔ Service-layer models
# ✔ Config objects
# ✔ ETL row models
# ✔ Cache values


# ============================================================
# 13. Mental Model (KEY TAKEAWAY)
# ============================================================

# dataclass answers:
# "I want a CLASS that mainly holds DATA,
#  not behavior."

# Less boilerplate.
# More clarity.
# Backend-friendly by default.
