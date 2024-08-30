def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix A:")
matrix_A = [list(map(int, input().split())) for _ in range(rows)]

print("Enter matrix B:")
matrix_B = [list(map(int, input().split())) for _ in range(rows)]

result = add_matrices(matrix_A, matrix_B)
print("Matrix addition result:")
print_matrix(result)
