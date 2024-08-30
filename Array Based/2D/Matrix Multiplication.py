def matrix_multiplication(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))
    return result

# Take input from user
rows_A = int(input("Enter number of rows for matrix A: "))
cols_A = int(input("Enter number of columns for matrix A (and rows for matrix B): "))
cols_B = int(input("Enter number of columns for matrix B: "))

print("Enter matrix A:")
matrix_A = [list(map(int, input().split())) for _ in range(rows_A)]

print("Enter matrix B:")
matrix_B = [list(map(int, input().split())) for _ in range(cols_A)]

result = matrix_multiplication(matrix_A, matrix_B)
print("Matrix multiplication result:")
print_matrix(result)
