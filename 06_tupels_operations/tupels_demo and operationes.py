
# # #empty tupel
# # empty_tuple=()
# # print(type(empty_tuple))
# # print(empty_tuple)

# # #numbers
# # num=(1,2,4,3,6,5)
# # print(num)

# # #text
# # num=("mouni","minnu","chinnu")
# # print(num)

# # #mixed
# # num=(1,2,4,3,6,5,"mouni","minnu","chinnu")
# # print(num)

# # #  tuples with class
# # tupel_num=tuple()
# # print(tupel_num)
# # print(type(tupel_num))


# #with numbers
# tuple_nums=tuple((1,2,3,7,8))
# print(tuple_nums)

# #with string
# tuple_nums=tuple(("mouni","chinnu","minnu","anuu"))
# print(tuple_nums)

# #mixed
# tuple_nums=tuple(("mouni","chinnu","minnu","anuu",1,2,3))
# print(tuple_nums)

# # tuple_nums=tuple((10))
# print(tuple_nums)#'int' object is not iterable
      
# tuple_nums=tuple((10,))
# print(tuple_nums)#(10,)

# tuple_nums=tuple(("mouni"))
# print(tuple_nums)#('m', 'o', 'u', 'n', 'i')

# #tupels and list

# list_=[10,20,30]
# tupels_num= tuple(list_)   
# print(tupels_num) 
# list_.append(30)
# print(list_)
# print(tupels_num)


# Accessing the data in list
tuple_nums = (10,20,30,40,50)
first_tuple_nums = tuple_nums[0]
last_tuple_nums = tuple_nums[-1]

# Indexing
print(first_tuple_nums)
print(last_tuple_nums)

# Slicing
tuple_nums = (10,20,30,40,50)
print(tuple_nums[:])
print(tuple_nums[1:4:1])
print(tuple_nums[1:4:-1])
print(tuple_nums[::-1])

# print(tuple_nums[10]) IndexError: tuple index out of range

# Looping can be done as it's an iterable
tuple_nums = [10,20,30,40,50]
for i in tuple_nums:
    print(i)
    
# perform any operations with operators
tuple_nums = tuple(range(0,36,5))
for i in tuple_nums:
    print(i*2)   

# perform some conditionals
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("Enter day name in a week: ")
if day in days:
    print("day is exist")
else:
    print("day is not exist")

# Duplicates are allowed
tuple_nums = [10,20,30,40,50,50,50,30]    
print(tuple_nums)





# Tuples Operations

tuple_nums = (10,20,30,40,50)
print(dir(tuple_nums))


# index() -> returns the index position of element, 
tuple_nums = (10,20,30,40,50)
print(tuple_nums.index(30))


# count() -> counts and returns number of times a element present
tuple_nums = (10,20,30,40,50,10)
print(tuple_nums.count(10))

# Tuples Packing nd Unpacking
person = ("John",25,"Python") # Packing
#person = ("John",25,"Python",25000)# ValueError: too many values to unpack (expected 3)
name,age,course = person # Unpacking

print(name)
print(age)
print(course)


t1 = ([10,20],[30,40],[50,60])
print(t1)
t1[0][0] = 100 # Valid -> Change List
print(t1)

t1 = ([10,20],[30,40],[50,60])
print(t1)
# t1[1] = [300,400] # Invalid -> change tuple
# TypeError: 'tuple' object does not support item assignment
print(t1)

#with list
l1 = [(10,20),(30,40),(50,60)]
print(l1)
# l1[0][0] = 100 #  Invalid 
# TypeError: 'tuple' object does not support item assignment
print(l1)

print(l1)
l1[1] = (300,400)
print(l1)

























