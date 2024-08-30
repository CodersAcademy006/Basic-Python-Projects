def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Take input from user
n = int(input("Enter the size of the identity matrix: "))
matrix = identity_matrix(n)
print("Identity matrix:")
print_matrix(matrix)
