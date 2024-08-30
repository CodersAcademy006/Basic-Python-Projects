def generate_pythagorean_triples(limit):
    triples = []
    for m in range(1, int(limit ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                if c <= limit:
                    triples.append((a, b, c))
    return triples

# Take input from user
limit = int(input("Enter the upper limit for Pythagorean triples: "))
print(f"Pythagorean triples up to {limit} are: {generate_pythagorean_triples(limit)}.")
