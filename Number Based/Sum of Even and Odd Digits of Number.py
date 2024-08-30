def sum_even_odd_digits(n):
    even_sum = sum(int(digit) for digit in str(n) if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in str(n) if int(digit) % 2 != 0)
    return even_sum, odd_sum

# Take input from user
num = int(input("Enter a number: "))
even_sum, odd_sum = sum_even_odd_digits(num)
print(f"The sum of even digits in {num} is {even_sum}.")
print(f"The sum of odd digits in {num} is {odd_sum}.")
