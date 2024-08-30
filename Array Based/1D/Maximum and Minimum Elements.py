def find_max_min(arr):
    return max(arr), min(arr)

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
max_element, min_element = find_max_min(arr)
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")
