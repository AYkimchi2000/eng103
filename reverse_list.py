def reverse_list(lst):
    """
    Reverses the order of elements in the given list.

    Args:
        lst (list): A list of elements to be reversed.

    This function modifies the original list in place and does not return anything.
    """
    left, right = 0, len(lst) - 1
    while left < right:
        # Swap the elements
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1