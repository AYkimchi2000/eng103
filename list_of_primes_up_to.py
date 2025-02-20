def list_of_primes_up_to(limit=100):
    """
    Returns a list of all prime numbers up to a given limit.
    """
    sieve = [False, False] + [True] * (limit - 1)
    
    for current_divisor in range(2, int(limit ** 0.5) + 1):
        if sieve[current_divisor]:
            for multiple in range(current_divisor * current_divisor, limit + 1, current_divisor):
                sieve[multiple] = False
    
    return [i for i in range(len(sieve)) if sieve[i]]
