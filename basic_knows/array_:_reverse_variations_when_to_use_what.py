'''
🧭 Final Notes — Reversing in Python: When to Use What

1️⃣ arr.reverse()
   • Reverses the list **in place** (modifies original).
   • Returns None.
   • ✅ Use when you just need to reverse the same list.

2️⃣ arr[::-1]
   • Returns a **new reversed copy** of the list.
   • Original list stays unchanged.
   • ✅ Use when you need both original and reversed versions.

3️⃣ reversed(arr)
   • Returns a **reverse iterator** (not a list).
   • Use list(reversed(arr)) to get a reversed list copy.
   • ✅ Use when you only need to iterate in reverse (memory efficient).

💡 Summary:
| Goal                                | Best Option       |
|------------------------------------|-------------------|
| Reverse original list (in-place)   | arr.reverse()     |
| Get reversed copy                  | arr[::-1]         |
| Iterate in reverse (no copy)       | reversed(arr)     |
'''
