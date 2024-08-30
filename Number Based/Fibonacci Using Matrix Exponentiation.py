import numpy as np

def fibonacci_matrix(n):
    def matrix_power(matrix, power):
        result = np.identity(len(matrix), dtype=object)
        base = matrix
        while power:
            if power % 2:
                result = np.dot(result, base)
            base = np.dot(base, base)
            power //= 2
        return result

    F = np.array([[1, 1], [1, 0]], dtype=object)
    if n == 0:
        return 0
    return matrix_power(F, n - 1)[0, 0]

# Take input from user
n = int(input("Enter the position in the Fibonacci sequence: "))
print(f"The {n}-th Fibonacci number is {fibonacci_matrix(n)}.")
