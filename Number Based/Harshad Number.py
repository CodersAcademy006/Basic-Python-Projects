# Function to check if a number is a Harshad number
def is_harshad(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum != 0 and n % digit_sum == 0
# Take input from user
num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
