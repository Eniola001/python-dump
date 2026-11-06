def rotate_list(nums, k):
    char_count = len(nums)

    if char_count == 0:
        return []

    k = k % char_count
    new_list = []
    start = char_count - k
    
    for i in range(start, start + char_count):
        index = i % char_count
        new_list.append(nums[index])
    return new_list
