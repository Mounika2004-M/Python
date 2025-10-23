
arr1=[1,4,6,7,3]
arr2=[9,335,67.5]

merged=arr1+arr2

for i in range(len(merged)):  
    for j in range(0,len(merged)-i-1):
        if merged[j]>merged[j+1]:
         merged[j], merged[j+1] = merged[j+1], merged[j]
print(merged)