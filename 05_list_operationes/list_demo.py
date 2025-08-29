# #empty list
# empty_list=[]
# print(empty_list)
# print(type(empty_list))

# #define list with number
# list=[10,20,30,40]
# print(list)

# #define list with text
# list_courses=["python", "java", "html","css","ml"]
# print(list_courses)

# #define combination of list and text
# list_comb=["python", "java", "html","css","ml",10,20,30,40 ]
# print(list_comb)

# #difine list inside the list(nested list)
# list_nest=["python", "java", "html","css","ml",[10,20,30,40] ]
# print(list_nest)

# #Indexing
# list=[10,20,30,40,50,60]
# print(list[3])
# print(list[4])

# #slicing
# list=[10,20,30,40,50,60]
# print(list[ : ])
# print(list[ 1:6:1])
# print(list[-1:-6:-1])

# #memory mangement with data
# num1=10
# num2=10
# print(id(num1))
# print(id(num2))

# list1=[10,20,30,40]
# list2=[10,20,30,40]
# print(id(list1))
# print(id(list2))

# #inside the list the elements are refernced
# print(id(list1[0]))
# print(id(list2[0]))

# print(id(num1))
# print(id(num2))
# print(id(list1[0]))
# print(id(list2[0]))

#looping can be done as it's iterabel
# list =[10,20,30,40,50]
# for i in list:
#     print(i)

#using range 
custem_list = list(range(0,26,1))
print(custem_list)


# perforem any operationes with operatoers

custem_list = list(range(0,26,5))
print(custem_list*2)#[0, 5, 10, 15, 20, 25, 0, 5, 10, 15, 20, 25] repeated two times

for i in custem_list:
    print(i*2)

# 10
# 20
# 30
# 40
# 50    its multipel by 2 inside the list elemenntes
 
 #perfoerm some condition
days  = ["sun", "mon", "tue","wed", "thu","fri","sat"]
day = input("enter day name in a weak")
if day in days:
    print("day exist")
else: 
    print("day is not exit")
 
#list allowes duplicates
list = [10,20,30,40,40]
print(list_name)
