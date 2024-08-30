def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix[0]
        matrix = list(zip(*matrix[1:]))[::-1]
    return result

# Take input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = [list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split())) for i in range(rows)]
print(f"Spiral order: {spiral_order(matrix)}")
