def flatten_matrix(matrix):
    return [elem for row in matrix for elem in row]

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
flattened = flatten_matrix(matrix)
print(f"Flattened matrix: {flattened}")
