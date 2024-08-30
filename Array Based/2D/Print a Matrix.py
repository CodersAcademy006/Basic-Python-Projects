def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
print("Matrix:")
print_matrix(matrix)
