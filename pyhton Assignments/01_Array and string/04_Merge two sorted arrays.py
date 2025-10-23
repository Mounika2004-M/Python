def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    merged = []

    # Traverse both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements of arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Add remaining elements of arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage
arr1 = [1, 2, 5, 7]
arr2 = [3, 4, 6, 8]

print(merge_sorted_arrays(arr1, arr2))


#USING BUBBELSORT


arr1=[1,4,6,7,3]
arr2=[9,335,67.5]

merged=arr1+arr2

for i in range(len(merged)):  
    for j in range(0,len(merged)-i-1):
        if merged[j]>merged[j+1]:
         merged[j], merged[j+1] = merged[j+1], merged[j]
print(merged)
        

