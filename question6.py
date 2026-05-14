def lists_to_dict(keys, values):
    return dict(zip(keys, values))

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

result = lists_to_dict(names, scores)
print(result) 