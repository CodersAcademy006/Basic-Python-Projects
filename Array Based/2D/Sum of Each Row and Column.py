def sum_rows_columns(matrix):
    rows_sum = [sum(row) for row in matrix]
    cols_sum = [sum(col) for col in zip(*matrix)]
    return rows_sum, cols_sum

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
row_sums, col_sums = sum_rows_columns(matrix)
print(f"Sum of each row: {row_sums}")
print(f"Sum of each column: {col_sums}")
