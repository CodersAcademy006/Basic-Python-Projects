def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Take input from user
arr1 = list(map(int, input("Enter elements of the first array separated by spaces: ").split()))
arr2 = list(map(int, input("Enter elements of the second array separated by spaces: ").split()))
print(f"Intersection of the two arrays: {intersection(arr1, arr2)}")
