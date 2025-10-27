def factorial_iterative(n):
    """
    Calculate factorial using an iterative (loop-based) approach.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print("Iterative:", factorial_iterative(5))


# ===========================================================================


def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    Base case: factorial(0) = 1
    Recursive case: factorial(n) = n * factorial(n-1)
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Example
print("Recursive:", factorial_recursive(5))
