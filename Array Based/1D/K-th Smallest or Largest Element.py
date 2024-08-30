def kth_smallest(arr, k):
    return sorted(arr)[k - 1]

def kth_largest(arr, k):
    return sorted(arr, reverse=True)[k - 1]

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
k = int(input("Enter the value of k: "))
print(f"{k}-th smallest element: {kth_smallest(arr, k)}")
print(f"{k}-th largest element: {kth_largest(arr, k)}")
