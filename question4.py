def get_odd_indices(numbers):
    indices = []
    for index, value in enumerate(numbers):
        if value % 2 != 0:
            indices.append(index)
    return indices

nums = [10, 15, 20, 25, 30]
print(get_odd_indices(nums))  