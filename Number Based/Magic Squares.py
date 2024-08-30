def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Magic square generation is only implemented for odd-order squares.")
    
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        i, j = (i - 1) % n, (j + 1) % n
        if magic_square[i][j]:
            i, j = (i + 2) % n, (j - 1) % n
    
    return magic_square

# Take input from user
n = int(input("Enter the order of the magic square (odd number): "))
magic_square = generate_magic_square(n)
for row in magic_square:
    print(row)
