def reverse_array(arr):
    return arr[::-1]

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Reversed array: {reverse_array(arr)}")
