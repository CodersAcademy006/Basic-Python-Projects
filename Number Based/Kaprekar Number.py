def is_kaprekar(n):
    square = n * n
    str_square = str(square)
    length = len(str(n))
    right_part = int(str_square[-length:]) if str_square[-length:] else 0
    left_part = int(str_square[:-length]) if str_square[:-length] else 0
    return n == (left_part + right_part)

# Take input from user
num = int(input("Enter a number: "))
if is_kaprekar(num):
    print(f"{num} is a Kaprekar number.")
else:
    print(f"{num} is not a Kaprekar number.")
