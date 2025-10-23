arr=[1,4,7,3,8,6,10,7]
unique_array = []
for num in arr:
    if num not in unique_array:
        unique_array.append(num)
sml=larg=unique_array[0]

for i in unique_array:
    if i>larg:
        larg=i 

    if i<sml:
        sml=i

secLarg_num=sml
for i in unique_array:
    if i>secLarg_num and i<larg:
        secLarg_num=i

third_num=sml
for i in unique_array:
    if i>third_num and i<secLarg_num :
        third_num=i

print("smallest number is:", sml)
print("largest number is:", larg)    
print("second largest number:", secLarg_num)
print(third_num)


arr=[1,7,5,3,8,6,4]
evenresult=[]
oddresult=[]

for i in arr:
     if i%2==0:
         evenresult.append(i)
         evenresult.sort()

     else:
         oddresult.append(i)
         oddresult.sort()

print(evenresult)
print(oddresult)
         
         
         
         
         



                                                                                                                                                                                 