#list operationes
# print(dir(list))


# append() operation
list_num =[10,20,30,40,50]
print(list_num)
list_num.append(60) # [10, 20, 30, 40, 50, 60]
print(list_num)
# list_num.append(70,80) #TypeError: list.append() takes exactly one argument (2 given)
# print(list_num)
list_num.append([70,80])# [10, 20, 30, 40, 50, 60, [70, 80]] its allow as nested list
print(list_num)
 
list_num.append("hello")
print(list_num)

#extend()  --> it can add only iterabel (like string list ) if we add elements are added as indivisuales not as nested

list_num =[10,20,30,40,50]
print(list_num)
# list_num.extend(60)#TypeError: 'int' object is not iterable
list_num.extend([60]) #[10, 20, 30, 40, 50, 60]
print(list_num)


list_num.extend([70,80,]) # [10, 20, 30, 40, 50, 60, 70, 80]
print(list_num)


# list_num.extend([70,80,],[90,100,]) # TypeError: list.extend() takes exactly one argument (2 given)
# print(list_num)

list_num.extend("hello") #[10, 20, 30, 40, 50, 60, 70, 80, 'h', 'e', 'l', 'l', 'o']
print(list_num)

# insert() --> based on index insert an element
list_num =[10,20,30,40,50]
print(list_num)
list_num.insert(0,5)
print(list_num)

list_num.insert(-1,60) #[5, 10, 20, 30, 40, 60, 50]
print(list_num)

list_num.insert(len(list_num),60)#[5, 10, 20, 30, 40, 60, 50, 60]
print(list_num) 

list_num.insert(10,90) #[5, 10, 20, 30, 40, 60, 50, 60, 90] ---> by default its added to  last
print(list_num) 

# pop () --> removes an element, by default last element
list_num =[10,20,30,40,50]
print(list_num)
removed_element=list_num.pop() #[10, 20, 30, 40]
print(removed_element) #50
print(list_num)


removed_element=list_num.pop(3) #[10, 20, 30]
print(removed_element) # 40
print(list_num)

# removed_element=list_num.pop(5) #IndexError: pop index out of range
# print(removed_element) 
# print(list_num)


# remove()--->removes matching values, its not index based its value based

list_num =[10,20,30,40,50]
print(list_num)
list_num.remove(30)#[10, 20, 40, 50]
print(list_num)

# list_num.remove(30,40)#TypeError: list.remove() takes exactly one argument (2 given)
# print(list_num)


#clear() --> remove all the  elementes

list_num =[10,20,30,40,50]
print(list_num)
list_num.clear()#[]
print(list_num)

#index() --> which returnus index position of element 
list_num =[10,20,30,40,50]
print(list_num)
print(list_num.index(20))#1

  # for multipel indexing
list_num =[10,20,30,40,50,60,20,80,90,20]
print(list_num)
print(list_num.index(20,2))#start 2 indexing
print(list_num.index(20,2,8))

# count()===> it counts and retuerns the number of times the element is present
list_num =[10,20,30,40,50,60,10,10,30,80,90,20,10]
print(list_num)
print(list_num.count(10))

#reverse() ===> reverse the element  of list and updates original 
list_num =[10,20,30,40,50,60,10,10,30,80,90,20,10]
print(list_num)
list_num.reverse()
print(list_num)

#slicing reverse the element  of list and don't updates original 
list_num =[10,20,30,40,50,60,10,10,30,80,90,20,10]
print(list_num)
print(list_num[::-1])
print(list_num)

#sort()===> sort the list , by default ascending order
list_num =[10,20,30,40,100,60,10,10,30,80,90,20,10]
print(list_num)
print(list_num.sort())# ascending order====>[10, 10, 10, 10, 20, 20, 30, 30, 40, 60, 80, 90, 100]
print(list_num)

list_num =[10,20,30,40,100,60,10,10,30,80,90,20,10]
print(list_num)
print(list_num.sort(reverse=True))# descending order====>[10, 10, 10, 10, 20, 20, 30, 30, 40, 60, 80, 90, 100]
print(list_num)

list_num =["minnu","anu","minnu","chinnu","veera","mouni"]
print(list_num)
print(list_num.sort())# ascending order
print(list_num)


list_num =["minnu","anu","minnu","chinnu","veera","mouni"]
print(list_num)
print(list_num.sort(reverse=True))# descending order====>[10, 10, 10, 10, 20, 20, 30, 30, 40, 60, 80, 90, 100]
print(list_num)

# mixed data
# list_num =["minnu","anu","minnu","chinnu","veera","mouni",10,20,30,40,100,60]
# print(list_num)
# print(list_num.sort())# TypeError: '<' not supported between instances of 'int' and 'str'
# print(list_num)


#  copy()  =====> create a shallow copy--> meaning when we modify shallow copy the originnal copy is not  affected

list_text =["minnu","anu","minnu","chinnu","veera","mouni"]
print(list_text)
bk_list_text=list_text.copy()#['minnu', 'anu', 'minnu', 'chinnu', 'veera', 'mouni']
print(bk_list_text)
bk_list_text.append("dummu")#soft copy() ---> use assignment operator
print(bk_list_text)#['minnu', 'anu', 'minnu', 'chinnu', 'veera', 'mouni', 'dummu']
print(list_text)#['minnu', 'anu', 'minnu', 'chinnu', 'veera', 'mouni']






