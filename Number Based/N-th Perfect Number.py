def nth_perfect_number(n):
    def is_perfect(num):
        return num == sum(i for i in range(1, num) if num % i == 0)
    
    count, num = 0, 2
    while count < n:
        if is_perfect(num):
            count += 1
        num += 1
    return num - 1

# Take input from user
n = int(input("Enter the position of the perfect number: "))
print(f"The {n}-th perfect number is {nth_perfect_number(n)}.")
