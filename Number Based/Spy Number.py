def is_spy(n):
    digits = [int(digit) for digit in str(n)]
    return sum(digits) == 1 or product(digits) == 1

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Take input from user
num = int(input("Enter a number: "))
if is_spy(num):
    print(f"{num} is a Spy number.")
else:
    print(f"{num} is not a Spy number.")
