def count_frequency(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

print(count_frequency("banana")) 