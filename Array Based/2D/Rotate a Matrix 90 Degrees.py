def rotate_matrix_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
rotated = rotate_matrix_90(matrix)
print("Matrix rotated 90 degrees:")
print_matrix(rotated)
