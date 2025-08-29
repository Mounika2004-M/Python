# without map
#input [1,2,3,4]---> output[1,4,9,16]
def sqare(numbers):
    squer_list=[]
    for n in numbers:
        squer_list.append(n*n)
    return squer_list

print(sqare([1,2,4,6]))
          

# with map
#synatx map(function, iterable)    ===> no condition only iterabel
print(map(lambda n: n * n , [1,2,3,6]))
            # o/p==> [1, 4, 16, 36]
            #     <map object at 0x000001F46AE2C400> 
print(list(map(lambda n: n * n , [1,2,3,6]))) # o/p==>[1, 4, 9, 36]

print(list(map(lambda n: n + n , [1,2,3,6])))

#without filter 
# even number
def even(number):
    evene_list=[]
    for  n in number:
        if n%2==0:
            evene_list.append(n)
    return evene_list
print(even([1,2,3,4,5,6,7,8,9,10]))

# with filter function 
#syntax  filter(function, iterable)   ====> iterable and condition
print(filter(lambda n: n%2==0, [1,2,3,4,56,7,8,9,]))
print(list(filter(lambda n: n%2==0, [1,2,3,4,56,7,8,9,])))

#without reduce
#factorial (5)
def fact(number):
    result=1
    for i in number:
        result=result*i
    return result
print( fact([1,2,4,5]))

# with reduce 
# reduce is a part of module so we shold import befor using it

from functools import reduce
print(reduce(lambda x,y: x*y, [1,2,3,4,56,7,8,9,]))









