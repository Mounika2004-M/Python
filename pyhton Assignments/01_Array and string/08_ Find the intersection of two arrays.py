arr1=[1,3,6,8,0,7,6,8]
arr2=[2,4,7,5,4,8]

intersection=[]
for i in arr1 :
    for j in arr2:
        if i == j :
            intersection.append(i)
print(intersection)



# Using Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

intersection = A & B 
print(intersection)  




arr1 = [1,3,6,8,0,7,6,8]
arr2 = [2,4,7,5,4,8]

intersection = []
for i in arr1:
    if i in arr2 and i not in intersection:
        intersection.append(i)

print(intersection)
