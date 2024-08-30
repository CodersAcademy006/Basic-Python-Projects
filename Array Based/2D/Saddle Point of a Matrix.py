def saddle_point(matrix):
    saddle_points = []
    for i in range(len(matrix)):
        row_min = min(matrix[i])
        row_min_index = matrix[i].index(row_min)
        column = [matrix[j][row_min_index] for j in range(len(matrix))]
        if row_min == max(column):
            saddle_points.append((i, row_min_index, row_min))
    return saddle_points

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
saddle_points = saddle_point(matrix)
print(f"Saddle points: {saddle_points}")
