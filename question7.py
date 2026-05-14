def manual_iterate(items):
    it = iter(items)
    
    while True:
        try:
            element = next(it)
            print(element)
        except StopIteration:
            break

my_list = [10, 20, 30]
manual_iterate(my_list)