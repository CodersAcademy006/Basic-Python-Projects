def move_zeroes(arr):
    non_zeroes = [x for x in arr if x != 0]
    zeroes = [0] * (len(arr) - len(non_zeroes))
    return non_zeroes + zeroes

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Array with zeroes moved to the end: {move_zeroes(arr)}")
