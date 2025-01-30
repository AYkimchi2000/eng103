def hailstone(n):
    """
    Compute the number of steps to reach 1 in a hailstone sequence.
    input: n (int): The starting positive integer.
    Returns: int: The number of steps to reach 1.
    """
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2 
        else:
            n = 3 * n + 1  
        steps += 1

    return steps

