def is_pronic(n):
    i = 0
    while i * (i + 1) < n:
        i += 1
    return i * (i + 1) == n

# Take input from user
num = int(input("Enter a number: "))
if is_pronic(num):
    print(f"{num} is a Pronic number.")
else:
    print(f"{num} is not a Pronic number.")
