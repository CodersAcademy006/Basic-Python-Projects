def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in s if char in vowels)
    num_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return num_vowels, num_consonants

# Take input from user
s = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(s)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
