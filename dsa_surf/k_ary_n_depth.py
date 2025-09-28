'''
Q1. What’s the total number of nodes in a perfect K-ary tree of depth N?
Ans:
- It forms a geometric series:  
  **1 + K + K² + … + Kᴺ = (Kⁿ⁺¹ – 1) / (K – 1)**

Example:
'''
# K = 3, N = 2 → 1 + 3 + 9 = 13
K, N = 3, 2
total_nodes = (K**(N+1) - 1) // (K - 1)
print(total_nodes)  # 13


'''
Q2. How many leaves are there at the bottom level (depth N)?
Ans:
- A perfect K-ary tree has **Kᴺ** leaves at depth N.
'''
K, N = 3, 2
leaves = K**N  # 3^2 = 9
print(leaves)



'''
Q3. How do you compute the number of internal nodes?
Ans:
- Internal nodes = Total – Leaves  
  → **I = (Kⁿ – 1) / (K – 1)**  
  (You can derive this from geometric properties.)
'''


'''
Q4. What’s the limit of Leaves / Total as N grows?
Ans:
- For large N,  
  **(Kᴺ) / ((Kⁿ⁺¹ – 1)/(K – 1)) ≈ 1/K**  
  → So most nodes are near the leaves.
'''



'''
Q6. How to model a K-ary tree in Python?
Ans:
- Use a class with a list of K children.
- Recursively build children up to desired depth.
'''
