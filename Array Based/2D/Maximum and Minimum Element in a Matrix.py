def max_min_matrix(matrix):
    flat_list = [elem for row in matrix for elem in row]
    return max(flat_list), min(flat_list)

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
max_element, min_element = max_min_matrix(matrix)
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")
