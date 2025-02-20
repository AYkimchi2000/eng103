def list_of_primes_up_to(limit=100):
    """
    Returns a list of all prime numbers up to a given limit.
    
    Parameters:
    limit (int): The upper bound for generating prime numbers. Default is 100.

    Returns:
    list: A list of prime numbers up to the given limit.
    """
    
    # Initialize a list with True values for potential primes, except for indices 0 and 1
    sieve = [False, False] + [True] * (limit - 1)
    
    # Set multiples of 2, 3, etc., to False
    for current_divisor in range(2, int(limit ** 0.5) + 1):
        if sieve[current_divisor]:
            for multiple in range(current_divisor * current_divisor, limit + 1, current_divisor):
                sieve[multiple] = False
                
    # List comprehension to return all prime numbers
    return [index for index, is_prime in enumerate(sieve) if is_prime]