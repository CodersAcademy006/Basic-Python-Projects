def second_largest(arr):
    unique_elements = list(set(arr))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[-2]

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Second largest element: {second_largest(arr)}")
