arr=[1,2,4,5,6]
n=6
excepted_value= n*(n+1)//2

appeared_value=0
for i in arr:
    appeared_value+=i
result= excepted_value -  appeared_value

print(result)





def find_two_missing_set(arr, n):
    full_set = set(range(1, n+1))
    print(full_set)
    arr_set = set(arr)
    print(arr)
    missing = list(full_set - arr_set)
    return missing

# Example
arr = [1, 2, 4, 6]  # n = 6
n = 6
print(find_two_missing_set(arr, n))  # Output: [3, 5]


