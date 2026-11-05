# Problem

# Given a matrix (a list containing rows of numbers), calculate and display the total of each row.
# Use this starting matrix: matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]].

# Examples
# Matrix above
# Row 1 total: 12
# Row 2 total: 9
# Row 3 total: 60

# Constraints
# Use nested loops.
# Do not use sum() or import libraries.
# Your solution should work for a matrix with a different number of rows.
    
# What This Tests
# Nested lists, nested loops, accumulators, and indexing.

matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30,]]

def row_sums(rows):
    row_num = 0
    for row in rows:
        total = 0
        row_num += 1
        for i in range(len(row)):
            total += row[i]
        print(f"Row {row_num} total: {total}")

row_sums(matrix)