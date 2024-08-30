def sum_of_elements(arr):
    return sum(arr)

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Sum of elements: {sum_of_elements(arr)}")
