def remove_duplicates(nums):
    no_duplicates = []
    for num in nums:
        if num not in no_duplicates:
            no_duplicates.append(num)
    return no_duplicates