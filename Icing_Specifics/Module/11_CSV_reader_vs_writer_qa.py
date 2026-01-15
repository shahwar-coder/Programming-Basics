'''
Q1. What is the main difference between csv.DictReader and csv.DictWriter?
A.
csv.DictReader is used to READ CSV files into Python dictionaries.
csv.DictWriter is used to WRITE Python dictionaries into CSV files.
DictReader is for ingestion, DictWriter is for export.
'''
# Example:
# reader = csv.DictReader(file)   # CSV → dict
# writer = csv.DictWriter(file, fieldnames=[...])  # dict → CSV


'''
Q2. Why is csv.DictReader preferred over csv.reader in backend systems?
A.
Because DictReader allows column-name based access instead of index-based access,
making the code safer, clearer, and less error-prone when CSV column order changes.
'''
# Example:
# row["email"]   # safer
# instead of
# row[2]         # fragile if columns shift


'''
Q3. Why must backend code NOT trust data read using csv.DictReader?
A.
Because all values are read as strings and CSV files may contain invalid,
missing, or malicious data. Validation and type casting are mandatory.
'''
# Example:
# age = int(row["age"])  # explicit casting
# if age < 0:
#     raise ValueError("Invalid age")


'''
Q4. Why does csv.DictWriter require fieldnames explicitly?
A.
Because DictWriter is schema-driven.
Explicit fieldnames enforce column order and output consistency.
'''
# Example:
# writer = csv.DictWriter(
#     f,
#     fieldnames=["id", "name", "email", "age"]
# )


'''
Q5. What happens if a dictionary has extra or missing keys when using DictWriter?
A.
Missing keys raise KeyError by default.
Extra keys are ignored unless extrasaction is configured.
'''
# Example:
# writer = csv.DictWriter(
#     f,
#     fieldnames=["id", "name"],
#     extrasaction="ignore"
# )


'''
Q6. Why is newline="" important when working with csv in Python?
A.
It prevents extra blank lines from appearing in CSV output,
especially on Windows systems.
'''
# Example:
# open("file.csv", "w", newline="", encoding="utf-8")
