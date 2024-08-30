def find_index(arr, x):
    return arr.index(x) if x in arr else -1

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
x = int(input("Enter the element to find: "))
index = find_index(arr, x)
print(f"Index of {x}: {index}")
