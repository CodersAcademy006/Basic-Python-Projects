def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
k = int(input("Enter the number of positions to rotate: "))
print(f"Rotated array: {rotate_array(arr, k)}")
