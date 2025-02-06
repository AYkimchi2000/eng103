def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2

some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)
print(result)