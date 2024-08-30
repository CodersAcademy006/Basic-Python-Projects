def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Take input from user
decimal = int(input("Enter a decimal number: "))
print(f"The binary value of decimal {decimal} is {decimal_to_binary(decimal)}.")
