'''
unnecessary_else_after_return (avoid)
'''
# - **Unnecessary `else` after `return`**: avoid redundant nesting.
  # Problem:
  def f(x):
      if x > 0:
          return "pos"
      else:
          return "non-pos"
  # Better:
  def f(x):
      if x > 0:
          return "pos"
      return "non-pos"
  # Step-by-step:
  # 1. Both behave the same, but second is clearer and avoids extra indentation.

# - **Misreading loop-else**: many expect `else` to run when loop had a truthy last item — it only runs when loop was NOT terminated by `break`.
# - **Overusing else**: sometimes an explicit `if` + early `return` or well-named helper makes code clearer than complex branching.
'''
