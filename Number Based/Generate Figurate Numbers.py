def figurate_number(n, s):
    if s == 3:  # Triangle number
        return n * (n + 1) // 2
    elif s == 4:  # Square number
        return n * n
    elif s == 5:  # Pentagon number
        return n * (3 * n - 1) // 2
    elif s == 6:  # Hexagon number
        return n * (2 * n - 1)
    elif s == 7:  # Heptagon number
        return n * (5 * n - 3) // 2
    elif s == 8:  # Octagon number
        return n * (3 * n - 2)
    else:
        raise ValueError("Unsupported number of sides")

# Take input from user
n = int(input("Enter the position of the figurate number: "))
s = int(input("Enter the number of sides of the polygon: "))

print(f"The {n}-th {s}-gon number is {figurate_number(n, s)}.")
