# ============================================================
# csv module in Python — Backend-Centric Guide
# ============================================================

# CSV = Comma Separated Values
# In backend systems, CSV is commonly used for:
# - Bulk uploads (users, products, orders)
# - Admin exports (reports, analytics)
# - Data migration / ETL pipelines
# - Interop with Excel / legacy systems

import csv

# ============================================================
# 1. Reading CSV (LOW-LEVEL, ORDER-BASED)
# ============================================================

# users.csv
# id,name,email,age
# 1,Rahul,rahul@mail.com,28
# 2,Amit,amit@mail.com,35

with open("users.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)            # skip header
    for row in reader:
        # row is a list of strings
        user_id, name, email, age = row
        age = int(age)               # backend MUST cast types

# ❌ fragile if column order changes


# ============================================================
# 2. Reading CSV with DictReader (BEST PRACTICE)
# ============================================================

with open("users.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # row is dict-like
        user = {
            "id": int(row["id"]),
            "name": row["name"],
            "email": row["email"],
            "age": int(row["age"]),
        }

# ✔ column-name based
# ✔ safer
# ✔ industry standard for backend


# ============================================================
# 3. Writing CSV (EXPORT / REPORTS)
# ============================================================

users = [
    {"id": 1, "name": "Rahul", "email": "rahul@mail.com", "age": 28},
    {"id": 2, "name": "Amit", "email": "amit@mail.com", "age": 35},
]

with open("export.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name", "email", "age"]
    )
    writer.writeheader()
    writer.writerows(users)

# ✔ deterministic column order
# ✔ clean exports


# ============================================================
# 4. Handling CSV Uploads (Backend Flow)
# ============================================================

"""
file = request.file                  # uploaded CSV
decoded = file.read().decode("utf-8").splitlines()
reader = csv.DictReader(decoded)

for row in reader:
    validate(row)
    save_to_db(row)
"""

# IMPORTANT:
# ✔ never trust CSV input
# ✔ validate each row
# ✔ stream line-by-line


# ============================================================
# 5. Validation (CRITICAL IN BACKEND)
# ============================================================

def validate_user(row):
    if not row.get("email"):
        raise ValueError("Email is required")
    if int(row["age"]) < 18:
        raise ValueError("User must be adult")

# Always validate before DB insert


# ============================================================
# 6. Large CSV Files (PERFORMANCE)
# ============================================================

# csv.reader / DictReader already stream rows
# DO NOT load entire CSV into memory

with open("big.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    batch = []

    for row in reader:
        batch.append(row)
        if len(batch) == 1000:
            bulk_insert(batch)    # DB bulk insert
            batch.clear()


# ============================================================
# 7. Dialects & Delimiters (REAL-WORLD DATA)
# ============================================================

# Not all CSVs use commas!

with open("data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        pass

# Other common delimiters:
# ","  ";"  "|"  "\t"


# ============================================================
# 8. Common Backend Pitfalls (VERY IMPORTANT)
# ============================================================

# ❌ Using .split(",")
# ❌ Ignoring encoding
# ❌ Forgetting newline=""
# ❌ Assuming correct data types
# ❌ Loading entire CSV in memory
# ❌ Skipping validation


# ============================================================
# 9. CSV vs JSON (Backend Decision)
# ============================================================

# CSV:
# ✔ lightweight
# ✔ Excel-friendly
# ❌ flat only
# ❌ no schema

# JSON:
# ✔ structured
# ✔ nested
# ✔ API-native
# ❌ larger payload


# ============================================================
# 10. Mental Model (KEY TAKEAWAY)
# ============================================================

# CSV handling in backend is NOT about files.
# It is about:
# ✔ streaming
# ✔ validation
# ✔ transformation
# ✔ performance
# ✔ safe persistence
