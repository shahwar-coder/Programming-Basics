'''
random module (Python) — Concise Summary

• Used to generate pseudo-random numbers (not truly random)
• Based on a deterministic algorithm (same seed → same results)
• Commonly used in games, simulations, sampling, testing

Key Functions:
• random()        → float between 0.0 and 1.0
• randint(a, b)   → integer between a and b (inclusive)
• randrange()     → integer from a range
• choice(seq️()     → random single element from sequence
• choices()       → random elements with repetition
• sample()        → random elements without repetition
• shuffle()       → randomly rearranges a list (in-place)
• uniform(a, b)   → random float between a and b

Seeding:
• seed(x)         → fixes randomness for reproducible output

Important Notes:
• Not suitable for security-related randomness
• For cryptography, use the secrets module instead
'''
