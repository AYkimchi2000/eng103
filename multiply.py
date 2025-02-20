# multiply.py
def multiply(a, b):
    """
    Multiplies two positive integers a and b using recursion and addition.

    Args:
    a (int): The first positive integer.
    b (int): The second positive integer.

    Returns:
    int: The product of a and b.

    Example:
    multiply(7, 4) returns 28.
    """
    if b == 1:
        return a
    return a + multiply(a, b - 1)