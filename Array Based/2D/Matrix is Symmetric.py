def is_symmetric(matrix):
    return matrix == transpose_matrix(matrix)

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
print(f"Matrix is symmetric: {is_symmetric(matrix)}")
