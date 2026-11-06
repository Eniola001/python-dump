def intersection(a, b):
    new_list = []

    for num in a:
        if num not in new_list and num in b:
            new_list.append(num)
    
    return new_list