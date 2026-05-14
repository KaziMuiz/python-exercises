def rotate_list(nums, k):
    n = len(nums)
    k = k % n  
    return nums[-k:] + nums[:-k]

numbers = [1, 2, 3, 4, 5]
print(rotate_list(numbers, 2))  