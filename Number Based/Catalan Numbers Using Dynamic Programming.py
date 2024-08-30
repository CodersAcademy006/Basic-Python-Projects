def catalan_number_dynamic(n):
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    return catalan[n]

# Take input from user
n = int(input("Enter the position of the Catalan number: "))
print(f"The {n}-th Catalan number is {catalan_number_dynamic(n)}.")
