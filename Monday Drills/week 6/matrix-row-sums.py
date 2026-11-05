# Problem
# Given a matrix (a list containing rows of numbers), 
# calculate and display the total of each row, the total of each column, 
# and the average of each row.

# Examples
# Starting matrix: matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
# Row 1 total: 12 | Row 1 average: 4.0
# Row 2 total: 9 | Row 2 average: 3.0
# Row 3 total: 60 | Row 3 average: 20.0
# Column 1 total: 13
# Column 2 total: 27
# Column 3 total: 41

matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
print(f"Starting matrix: matrix = {matrix}")

row_number = 0
column_number = 0

for row in matrix:
    row_total = 0
    row_number += 1
    for number in row:
        row_total += number
    row_average = row_total / len(row)
    print(f"Row {row_number} total: {row_total} | Row {row_number} average: {row_average}")

if matrix:
    for i in range(len(matrix[0])):
        column_total = 0
        column_number += 1
        for column in matrix:
            column_total += column[i]
        print(f"Column {column_number} total: {column_total}")