from collections import Counter

# ================
# BASIC CREATION
# ================
c = Counter("banana")  
# Useful for: ANY frequency problem (anagrams, sliding window, top K, etc.)

print("Counter:", c)
# Counter({'a': 3, 'n': 2, 'b': 1})


# ============================
# 1️⃣ most_common(n)
# ============================
# Returns top n elements by frequency (sorted)
print("Most Common 2:", c.most_common(2))
# Useful for: TOP K FREQUENT ELEMENTS, sorting by count


# ============================
# 2️⃣ elements()
# ============================
# Returns iterator repeating elements by their frequency
print("Elements:", list(c.elements()))
# Useful for: Reconstructing lists from frequency maps


# ============================
# 3️⃣ update(iterable / dict)
# ============================
c2 = Counter("abc")
c2.update("aa")  
print("After update:", c2)
# Useful for: Adding counts when expanding a window or adding new data


# ============================
# 4️⃣ subtract(iterable / dict)
# ============================
c3 = Counter("banana")
c3.subtract("an")  
print("After subtract:", c3)
# Useful for: Removing counts when shrinking a sliding window (anagrams)


# ============================
# 5️⃣ items(), keys(), values()
# ============================
print("Items:", list(c.items()))
print("Keys:", list(c.keys()))
print("Values:", list(c.values()))
# Useful for: Iterating through frequency maps like normal dict


# ============================
# 6️⃣ copy()
# ============================
c_copy = c.copy()
print("Copy:", c_copy)
# Useful for: Keeping original counter safe during modifications


# ============================
# 7️⃣ Arithmetic on Counters
# ============================

# ➕ Addition
c_add = Counter("aab") + Counter("bcc")
print("Addition:", c_add)
# Useful for: Merging frequency maps (rare but handy)

# ➖ Subtraction (removes negative or zero counts automatically)
c_sub = Counter("banana") - Counter("an")
print("Subtraction:", c_sub)
# Useful for: Building result after removing required elements


# ============================
# 8️⃣ Access non-existing key
# ============================
print("Missing key result:", c["z"])  # returns 0, not error
# Useful for: Avoiding KeyErrors during frequency checking


# ============================
# 9️⃣ Convert Counter to dict
# ============================
print("As dict:", dict(c))
# Useful for: Problems requiring normal dictionary output


# ============================
# 🔟 Clear Counter (optional)
# ============================
# c.clear()
# Useful for: Resetting counts cleanly
