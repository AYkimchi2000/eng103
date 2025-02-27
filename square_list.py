# square_list.py
def square_list(nums):
    """
    Takes a list of numbers and replaces each value with its square.

    Args:
        nums (list): A list of numerical values to be squared.

    This function modifies the original list in place and does not return anything.
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2