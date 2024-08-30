def average_of_elements(arr):
    return sum(arr) / len(arr)

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Average of elements: {average_of_elements(arr)}")
