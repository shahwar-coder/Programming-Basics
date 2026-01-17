# ============================================================
# tabulate in Python — Backend-Oriented Guide
# ============================================================

# tabulate is used to DISPLAY structured data (lists, dicts, DB rows)
# in a clean, readable TABLE format.
#
# IMPORTANT:
# tabulate is for:
# ✔ debugging
# ✔ admin tools
# ✔ internal scripts
# ✔ CLI utilities
# ❌ NOT for APIs / production responses (use JSON there)

from tabulate import tabulate


# ============================================================
# 1. WHY tabulate exists (Backend reality)
# ============================================================

# Backend developers constantly inspect:
# - DB query results
# - CSV rows
# - API responses
# - Logs
#
# Printing raw dicts/lists is unreadable.
# tabulate turns data → readable tables.


# ============================================================
# 2. Basic usage with list of lists
# ============================================================

data = [
    [1, "Rahul", 28],
    [2, "Amit", 35],
]

headers = ["id", "name", "age"]

print(tabulate(data, headers=headers))

# Output:
# id  name    age
# --  ------  ---
# 1   Rahul   28
# 2   Amit    35


# ============================================================
# 3. MOST COMMON backend usage: list of dicts
# ============================================================

users = [
    {"id": 1, "name": "Rahul", "email": "rahul@mail.com"},
    {"id": 2, "name": "Amit", "email": "amit@mail.com"},
]

print(tabulate(users, headers="keys"))

# ✔ Automatically uses dict keys as columns
# ✔ Perfect for inspecting API / DB data


# ============================================================
# 4. Choosing table formats (IMPORTANT)
# ============================================================

print(tabulate(users, headers="keys", tablefmt="grid"))
print(tabulate(users, headers="keys", tablefmt="github"))
print(tabulate(users, headers="keys", tablefmt="psql"))
print(tabulate(users, headers="keys", tablefmt="plain"))

# Backend tip:
# - plain / psql → logs
# - github → README / docs
# - grid → CLI tools


# ============================================================
# 5. Backend debugging pattern (VERY COMMON)
# ============================================================

def debug_print(title, rows):
    print(f"\n--- {title} ---")
    print(tabulate(rows, headers="keys", tablefmt="psql"))

# Example:
debug_print("Fetched Users", users)


# ============================================================
# 6. tabulate with CSV data
# ============================================================

import csv

with open("users.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(tabulate(rows, headers="keys"))

# ✔ Perfect for verifying CSV ingestion logic


# ============================================================
# 7. tabulate with DB query results
# ============================================================

# Typical DB result:
rows = [
    (1, "Order-1", 500),
    (2, "Order-2", 900),
]

headers = ["id", "order_name", "amount"]

print(tabulate(rows, headers=headers, tablefmt="psql"))

# ✔ Inspect SQL query output quickly


# ============================================================
# 8. Limiting rows (BACKEND SAFETY)
# ============================================================

# NEVER print huge datasets fully
print(tabulate(users[:5], headers="keys"))

# Always slice before printing


# ============================================================
# 9. tabulate vs pandas vs prettytable
# ============================================================

# tabulate:
# ✔ lightweight
# ✔ minimal dependency
# ✔ perfect for backend debugging

# pandas:
# ✔ analytics-heavy
# ❌ heavy for backend runtime

# prettytable:
# ✔ similar to tabulate
# ❌ less flexible formats


# ============================================================
# 10. What NOT to do in production
# ============================================================

# ❌ Do not return tabulate output in APIs
# ❌ Do not log massive tables
# ❌ Do not use for frontend formatting

# APIs → JSON
# Logs → structured logs
# tabulate → humans only


# ============================================================
# 11. Real backend use cases
# ============================================================

# ✔ Admin CLI tools
# ✔ One-off data migration scripts
# ✔ Debugging ETL pipelines
# ✔ Verifying CSV / JSON ingestion
# ✔ Internal developer utilities


# ============================================================
# 12. Mental Model (KEY TAKEAWAY)
# ============================================================

# tabulate is NOT a data tool.
# It is a VISUALIZATION tool for developers.

# Use it when:
# "I need to SEE this data clearly."
