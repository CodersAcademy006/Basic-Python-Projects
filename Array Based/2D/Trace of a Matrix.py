def matrix_trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
print(f"Trace of the matrix: {matrix_trace(matrix)}")
