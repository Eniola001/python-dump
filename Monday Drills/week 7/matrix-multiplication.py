# Problem
# Given two matrices, A and B, calculate their product matrix.
# Matrix multiplication is possible only if the number of columns in A equals the number of rows in B.

# Examples
# Matrix A: [[1, 2], [3, 4]]
# Matrix B: [[5, 6], [7, 8]]
# Product Matrix:
# [19, 22]
# [43, 50]
# (Explanation: 1×5 + 2×7 = 19; 1×6 + 2×8 = 22, etc.)

# Constraints
# Use nested loops (three levels of loops are needed).
# Do not import libraries such as numpy.
# Do not use list comprehensions.
# Dynamically build the result matrix based on the dimensions of A and B.
# Do not hardcode the answer.


matrix_1 = [[1, 2], [3, 4]]
matrix_2 = [[5, 6], [7, 8]]

product = []

for i in range(len(matrix_1)):
    row_product = []

    for j in range(len(matrix_2[0])):
        total = 0

        for k in range(len(matrix_2)):
            total += matrix_1[i][k] * matrix_2[k][j]
        
        row_product.append(total)

    product.append(row_product)

print("Product Matrix:")
for row in product:
    print(row)