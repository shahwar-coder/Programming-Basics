# ============================================================
# csv.DictReader vs csv.DictWriter — Backend Mental Model
# ============================================================

import csv

# CORE IDEA:
# DictReader  → CSV → Python dicts   (INPUT / INGESTION)
# DictWriter  → Python dicts → CSV   (OUTPUT / EXPORT)

# Think:
# DictReader = "READ & TRUST NOTHING"
# DictWriter = "WRITE & CONTROL FORMAT"


# ============================================================
# 1. csv.DictReader (READING CSV)
# ============================================================

# CSV file:
# id,name,email,age
# 1,Rahul,rahul@mail.com,28

with open("users.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # reader.fieldnames → column names detected from header
    print(reader.fieldnames)  # ['id', 'name', 'email', 'age']

    for row in reader:
        # row is a dict-like object
        # {'id': '1', 'name': 'Rahul', 'email': 'rahul@mail.com', 'age': '28'}

        # Backend work:
        # - validate
        # - cast types
        # - store in DB
        user = {
            "id": int(row["id"]),
            "name": row["name"],
            "email": row["email"],
            "age": int(row["age"])
        }

# ------------------------------------------------------------
# DictReader characteristics
# ------------------------------------------------------------

# ✔ Reads header automatically
# ✔ Column-name based access
# ✔ Order-independent
# ✔ Streams row-by-row (memory safe)
# ❌ All values are strings
# ❌ No validation (you must do it)


# ============================================================
# 2. csv.DictWriter (WRITING CSV)
# ============================================================

users = [
    {"id": 1, "name": "Rahul", "email": "rahul@mail.com", "age": 28},
    {"id": 2, "name": "Amit", "email": "amit@mail.com", "age": 35},
]

with open("export.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "name", "email", "age"]
    )

    writer.writeheader()     # writes CSV header
    writer.writerows(users)  # writes multiple rows

# ------------------------------------------------------------
# DictWriter characteristics
# ------------------------------------------------------------

# ✔ You control column order
# ✔ Predictable output
# ✔ Clean exports
# ❌ Missing keys → KeyError (unless handled)
# ❌ Extra keys are ignored by default


# ============================================================
# 3. Handling missing / extra fields (IMPORTANT)
# ============================================================

writer = csv.DictWriter(
    f,
    fieldnames=["id", "name", "email", "age"],
    extrasaction="ignore"   # ignore extra keys safely
)

# extrasaction="raise"  → default, raises error


# ============================================================
# 4. Reader vs Writer (SIDE-BY-SIDE)
# ============================================================

# DictReader:
# - Used for input
# - Reads CSV → dict
# - Header-driven
# - Untrusted data

# DictWriter:
# - Used for output
# - Writes dict → CSV
# - Schema-driven
# - Trusted data


# ============================================================
# 5. Backend Flow (REAL WORLD)
# ============================================================

"""
UPLOAD CSV
   ↓
DictReader
   ↓
Validate + Transform
   ↓
Save to DB
   ↓
DictWriter (optional export / report)
"""


# ============================================================
# 6. Common Backend Mistakes
# ============================================================

# ❌ Using csv.reader instead of DictReader
# ❌ Trusting CSV input
# ❌ Not validating types
# ❌ Not fixing column order in DictWriter
# ❌ Forgetting newline=""


# ============================================================
# 7. Mental Model (KEY TAKEAWAY)
# ============================================================

# DictReader:
# "Read data I DO NOT trust"

# DictWriter:
# "Write data I CONTROL"
