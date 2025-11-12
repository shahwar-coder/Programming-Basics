'''
⏱️ TIME COMPLEXITY RANKING (from best to worst)

1️⃣ O(1) — Constant Time
   → Execution time does NOT depend on input size.
   Example: accessing arr[0], checking x % 2, assigning a variable.

2️⃣ O(log n) — Logarithmic Time
   → Input reduces by half each step.
   Example: binary search, finding element in balanced BST.

3️⃣ O(n) — Linear Time
   → Time grows directly with input size.
   Example: single loop over list, sum(arr), count True values.

4️⃣ O(n log n) — Linearithmic Time
   → Common in efficient sorting algorithms.
   Example: merge sort, quicksort (average), heap sort.

5️⃣ O(n²) — Quadratic Time
   → Nested loops over same list size.
   Example: bubble sort, comparing every pair of elements.

6️⃣ O(n³) — Cubic Time
   → Triple nested loops.
   Example: some brute-force 3D matrix operations.

7️⃣ O(2ⁿ) — Exponential Time
   → Doubles with each additional element.
   Example: recursive subset generation, naive Fibonacci recursion.

8️⃣ O(n!) — Factorial Time
   → Permutations or brute-force over all arrangements.
   Example: generating all permutations of a string.

✅ Summary (fast → slow):
O(1)  <  O(log n)  <  O(n)  <  O(n log n)  <  O(n²)  <  O(n³)  <  O(2ⁿ)  <  O(n!)

💡 Rule of thumb:
- Aim for O(1) or O(n) in most coding problems.
- O(n log n) is usually acceptable for sorting or complex searches.
- Avoid O(n²)+ unless input size is very small.
'''
