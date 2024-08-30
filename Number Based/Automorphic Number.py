def is_happy(n):
    def sum_of_squares(x):
        return sum(int(digit) ** 2 for digit in str(x))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1

# Take input from user
num = int(input("Enter a number: "))
if is_happy(num):
    print(f"{num} is a Happy number.")
else:
    print(f"{num} is not a Happy number.")
