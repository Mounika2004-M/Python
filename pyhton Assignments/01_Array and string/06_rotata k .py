def rotate_array(arr, k):
    n = len(arr)
    k = k % n   # to handle cases where k > n
    return arr[-k:] + arr[:-k]

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
k = 6
print(rotate_array(arr, k))