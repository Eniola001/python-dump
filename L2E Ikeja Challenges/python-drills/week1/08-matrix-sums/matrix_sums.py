def matrix_sums(matrix):
    rows = []
    columns = []

    for row in matrix:
        row_total = 0
        for i in range(len(row)):
            row_total += row[i]
        rows.append(row_total)

    if matrix:
        for i in range(len(matrix[0])):
            column_total = 0
            for column in matrix:
                column_total += column[i]
            columns.append(column_total)    

    result = (rows, columns)
    return result

print(matrix_sums([[1, 2], [3, 4]]))