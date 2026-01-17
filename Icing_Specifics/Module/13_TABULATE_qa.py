'''
Q1. What is the `tabulate` library used for in Python?
A.
`tabulate` is used to display structured data (lists, dicts, rows)
in a clean, readable table format for humans.
It is mainly for debugging, CLI tools, and internal scripts.
'''
# Example:
# from tabulate import tabulate
# data = [[1, "Rahul", 28], [2, "Amit", 35]]
# headers = ["id", "name", "age"]
# print(tabulate(data, headers=headers))


'''
Q2. Why is `tabulate` useful for backend developers?
A.
Backend developers often inspect database rows, CSV data, or API responses.
`tabulate` makes this data easy to read compared to raw lists or dicts.
'''
# Example:
# users = [
#     {"id": 1, "name": "Rahul"},
#     {"id": 2, "name": "Amit"}
# ]
# print(tabulate(users, headers="keys"))


'''
Q3. How does `tabulate` work with a list of dictionaries?
A.
When given a list of dictionaries, `tabulate` can automatically
use dictionary keys as column headers using headers="keys".
'''
# Example:
# users = [
#     {"id": 1, "email": "a@mail.com"},
#     {"id": 2, "email": "b@mail.com"}
# ]
# print(tabulate(users, headers="keys"))


'''
Q4. What are table formats in `tabulate`, and why do they matter?
A.
Table formats control how the table looks (grid, plain, psql, github).
Different formats are useful for logs, CLI tools, or documentation.
'''
# Example:
# print(tabulate(users, headers="keys", tablefmt="psql"))
# print(tabulate(users, headers="keys", tablefmt="grid"))


'''
Q5. Can `tabulate` be used with CSV or database data?
A.
Yes. `tabulate` is commonly used after reading CSV files
or fetching rows from a database to visually inspect the data.
'''
# Example:
# import csv
# with open("users.csv") as f:
#     rows = list(csv.DictReader(f))
# print(tabulate(rows, headers="keys"))


'''
Q6. When should `tabulate` NOT be used?
A.
`tabulate` should not be used for API responses or production output.
APIs should return JSON; `tabulate` is only for human-readable display.
'''
# Example:
# ❌ Do not do this in APIs:
# return tabulate(data, headers="keys")
#
# ✅ Do this instead:
# return json.dumps(data)
