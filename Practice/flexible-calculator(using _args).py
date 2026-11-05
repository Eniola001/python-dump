def calculate_stats(*args):
    if len(args) == 0:
        return "No input"

    total = 0
    maximum = args[0]
    minimum = args[0]
    for arg in args:
        total += arg
        if arg > maximum:
            maximum = arg
        if arg < minimum:
            minimum = arg
    average = total/len(args)
    return f"Sum: {total} \nAverage: {average} \nMaximum: {maximum} \nMinimum: {minimum}"
        
print(calculate_stats(1,2,3,4,5))
print(calculate_stats())
