def most_frequent(items):
    count = {}

    for item in items:
        count[item] = count.get(item, 0) + 1

    highest = 0
    most_common = None

    for item in items:
        if count[item] > highest:
            highest = count[item]
            most_common = item

    return most_common