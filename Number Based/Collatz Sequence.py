def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

# Take input from user
num = int(input("Enter a number: "))
print(f"The Collatz sequence for {num} is: {collatz_sequence(num)}.")
