def centered_polygonal_number(n, s):
    return (s - 2) * (n**2) - (s - 4) * n + 1

# Take input from user
n = int(input("Enter the position of the centered polygonal number: "))
s = int(input("Enter the number of sides of the polygon: "))

print(f"The {n}-th centered {s}-gon number is {centered_polygonal_number(n, s)}.")
