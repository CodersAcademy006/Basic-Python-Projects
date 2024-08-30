def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Take input from user
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if can_form_triangle(a, b, c):
    print("The lengths can form a triangle.")
else:
    print("The lengths cannot form a triangle.")
