def find_second_largest(numbers):
    largest = second_largest = float('-inf')

    for n in numbers:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n
            
    return second_largest
nums = [10, 20, 4, 45, 99]
print(find_second_largest(nums))  