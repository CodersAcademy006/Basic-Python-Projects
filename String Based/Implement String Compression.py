def string_compression(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return ''.join(compressed) if len(''.join(compressed)) < len(s) else s

# Take input from user
s = input("Enter a string: ")
print(f"Compressed string: {string_compression(s)}")
