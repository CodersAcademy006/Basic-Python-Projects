def matrices_equal(A, B):
    return A == B

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix A:")
matrix_A = [list(map(int, input().split())) for _ in range(rows)]

print("Enter matrix B:")
matrix_B = [list(map(int, input().split())) for _ in range(rows)]

print(f"Matrices are equal: {matrices_equal(matrix_A, matrix_B)}")
