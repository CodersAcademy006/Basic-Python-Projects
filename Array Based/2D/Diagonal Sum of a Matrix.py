def diagonal_sum(matrix):
    primary_diagonal = sum(matrix[i][i] for i in range(len(matrix)))
    secondary_diagonal = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
    return primary_diagonal, secondary_diagonal

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
primary_sum, secondary_sum = diagonal_sum(matrix)
print(f"Primary diagonal sum: {primary_sum}")
print(f"Secondary diagonal sum: {secondary_sum}")
