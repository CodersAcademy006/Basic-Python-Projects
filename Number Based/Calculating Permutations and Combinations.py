import math

def permutations(n, r):
    return math.perm(n, r)

def combinations(n, r):
    return math.comb(n, r)

# Take input from user
n = int(input("Enter the total number of items (n): "))
r = int(input("Enter the number of items to choose (r): "))
print(f"Permutations (P(n, r)) = {permutations(n, r)}")
print(f"Combinations (C(n, r)) = {combinations(n, r)}")
