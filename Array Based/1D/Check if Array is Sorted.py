def is_sorted(arr):
    return arr == sorted(arr)

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Array is sorted: {is_sorted(arr)}")
