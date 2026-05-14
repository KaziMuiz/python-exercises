def square_evens(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

nums = [1, 2, 3, 4, 5, 6]
print(square_evens(nums))  
