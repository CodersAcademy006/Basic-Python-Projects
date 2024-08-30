def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        return sorted_arr[mid]

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Median: {find_median(arr)}")
