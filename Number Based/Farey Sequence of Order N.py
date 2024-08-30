from fractions import Fraction

def farey_sequence(n):
    farey_seq = {Fraction(0, 1), Fraction(1, 1)}
    for d in range(1, n + 1):
        for num in range(1, d):
            frac = Fraction(num, d)
            if frac not in farey_seq:
                farey_seq.add(frac)
    return sorted(farey_seq)

# Take input from user
order = int(input("Enter the order of the Farey sequence: "))
print(f"The Farey sequence of order {order} is: {farey_sequence(order)}.")
