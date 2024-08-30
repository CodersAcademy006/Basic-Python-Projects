def is_valid_ipv4(s):
    parts = s.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
            return False
    return True

# Take input from user
s = input("Enter an IP address: ")
print(f"String is a valid IPv4 address: {is_valid_ipv4(s)}")
