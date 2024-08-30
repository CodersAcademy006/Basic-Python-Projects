from collections import Counter

def count_occurrences(arr):
    return dict(Counter(arr))

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Occurrences of each element: {count_occurrences(arr)}")
