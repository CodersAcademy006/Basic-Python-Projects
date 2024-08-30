def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
transposed = transpose_matrix(matrix)
print("Transposed matrix:")
print_matrix(transposed)
