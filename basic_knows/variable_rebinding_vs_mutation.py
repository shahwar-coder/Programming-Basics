# 🔑 Variable Rebinding vs Mutation

# • Rebinding → variable points to a new object.
# • Mutation  → object itself changes, variable still points to same object.

# --- Example of Mutation ---
lst = [1, 2]
lst2 = lst       # both point to same list
lst.append(3)    # mutates the list in place
print(lst2)      # [1, 2, 3]
# Reason: same object shared, so change is visible through both names.

# --- Example of Rebinding ---
lst = [1, 2]
lst2 = lst       # both point to same list initially
lst = [1, 2, 3]  # rebinding lst → new object
print(lst2)      # [1, 2]
# Reason: lst2 still points to old list, lst now points to a new one.
