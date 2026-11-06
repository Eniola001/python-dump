def find_missing(nums):
    list_checker = []
    for i in range(min(nums), max(nums) + 1):
        list_checker.append(i)
    for num in list_checker:
        if num not in nums:
            return num