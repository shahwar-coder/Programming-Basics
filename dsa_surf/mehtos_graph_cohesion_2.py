'''
Q1. What is a method graph?
Ans:
- A graph where each method is a **node**.
- An **edge** exists between two methods if they directly share something (like an instance variable).
'''


'''
Q2. What does maximal cohesion mean in this model?
Ans:
- It means **every method is connected to every other method** → a **complete graph (Kₙ)**.
'''
Example: If a class has 4 methods:
- Maximal cohesion = all pairs connected = 6 edges



'''
Q3. How do you compute number of direct connections?
Ans:
- It’s the number of **unordered pairs** of n nodes:
  →  C(n, 2) = n(n–1)/2
'''



'''
Q4. What’s the difference between direct and indirect connections?
Ans:
- Direct → immediate edge between methods.
- Indirect → connection through a path of other methods.

In Kₙ, all pairs are directly connected, so indirect links aren't needed.
'''



'''
Q5. What's the ordered-pair trap?
Ans:
- Using n(n–1) counts **ordered** pairs (A→B ≠ B→A).
- Use n(n–1)/2 unless problem explicitly asks for directed or ordered connections.
'''
