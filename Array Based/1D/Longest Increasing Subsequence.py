def longest_increasing_subsequence(arr):
    if not arr:
        return []
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    max_length = max(dp)
    lis = []
    for i in range(n - 1, -1, -1):
        if dp[i] == max_length:
            lis.append(arr[i])
            max_length -= 1
    return lis[::-1]

# Take input from user
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"Longest increasing subsequence: {longest_increasing_subsequence(arr)}")
