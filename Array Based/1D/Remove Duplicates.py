def remove_duplicates(arr):
    return list(set(arr))

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Array with duplicates removed: {remove_duplicates(arr)}")
