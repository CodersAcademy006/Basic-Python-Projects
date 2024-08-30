import math

def area_of_triangle(a, b, c):
    # Use Heron's formula
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Take input from user
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if can_form_triangle(a, b, c):
    area = area_of_triangle(a, b, c)
    print(f"The area of the triangle is {area:.2f}.")
else:
    print("The given sides do not form a triangle.")
