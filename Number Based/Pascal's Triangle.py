def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

# Take input from user
num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
