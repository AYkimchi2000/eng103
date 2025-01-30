def fib(x):
    """
    returns corresponding fib number given the index
    input: index number
    return: fib number at the given index 
    """
    fibseq = [1, 1]
    if x == 1:
        return 1
    if x == 2:
        return 1
    counter1 = 0
    counter2 = 1
    for i in range(x-2):
        next_fib = fibseq[counter1] + fibseq[counter2]
        counter1 += 1 
        counter2 += 1
        fibseq.append(next_fib)
    output_fib = fibseq[x-3] + fibseq[x-2]
    return output_fib


