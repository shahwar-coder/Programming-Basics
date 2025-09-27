'''
Q1. What is Method Graph Cohesion (MGC)?
Ans:
- A design analysis technique:
  → Model methods as nodes  
  → Add edges between methods if they **access the same field**  
- The goal is to assess how tightly methods relate.
'''



'''
Q2. What does high cohesion look like in a method graph?
Ans:
- All methods are connected (directly or indirectly) → one connected component.
- Suggests methods belong together and share purpose.
'''
# Example: All 5 methods share at least one common field → one big connected component.



'''
Q3. What does **low cohesion** mean in the graph?
Ans:
- The graph has **multiple disconnected components**.
- Methods don’t share fields → possibly unrelated responsibilities.
- Suggests class may be doing "too much" → consider splitting it.
'''



'''
Q4. What do connected components represent?
Ans:
- A **connected component** is a cluster of methods that are all reachable from each other (via shared fields).
- Each component = group of methods that are "logically together".
'''



'''
Q5. How is MGC useful in software design?
Ans:
- Detects **poorly cohesive classes** early.
- Helps identify:
   • Code smells
   • Opportunities to refactor
   • When a class violates single responsibility
'''



'''
Q6. Quick checklist for MGC analysis:
✔ Model methods as nodes  
✔ Add edge if they use same field  
✔ Count connected components  
✔ 1 component = cohesive  
✔ >1 → refactor candidate  
'''
  
