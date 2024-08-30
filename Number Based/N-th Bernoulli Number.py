from sympy import bernoulli

def nth_bernoulli_number(n):
    return bernoulli(n)

# Take input from user
n = int(input("Enter the position of the Bernoulli number: "))
print(f"The {n}-th Bernoulli number is {nth_bernoulli_number(n)}.")
