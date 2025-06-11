'''
1. Grading Function
Task:
Write a function get_grade(score: int) -> str that returns a letter grade for a numeric score (0–100) following these rules:

90–100 → "A"

80–89 → "B"

70–79 → "C"

60–69 → "D"

0–59 → "F"

If score is outside 0–100, raise a ValueError. Use an if/elif/else chain.

# Example 1
print(get_grade(95))  # "A"

# Example 2
print(get_grade(82))  # "B"

# Example 3
print(get_grade(59))  # "F"

# Example 4
print(get_grade(150))  # raises ValueError
'''

def get_grade(score: int)->str:
    """Return the grade obtained by student"""
    assert 0<=score<=100, "Score can only be between 0-100" # assert can be replaced with ValueError raising , if put to production.
    if 90<=score<=100:
        return "A"
    elif 80<=score<=89:
        return "B"
    elif 70<=score<=79:
        return "C"
    elif 60<=score<=69:
        return "D"
    else: # here elif not required to check <=59 as it has to be less than 59 now, if not in range 0-100, assert will have already handled it.
        return "F"

def main():
    score=int(input("Enter Score : "))
    print(get_grade(score))

if __name__=="__main__":
    main()
