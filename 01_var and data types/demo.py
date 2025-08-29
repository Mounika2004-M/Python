print("hello")
print(9)
a=10
b=20
print(a+b)


import keyword
print(keyword.kwlist)

from math import sqrt
print(sqrt(16))

#storing  data-- type of data

s_name1= "minnu"
print(type(s_name1))
print(id(s_name1))

s_name2= "chinnu"
print(id(s_name2))

s_age = 20
print(type(s_age))
print(id(s_age))

s_age1 = 20
print(id(s_age1))

s_cgpa= 8.5
print(type(s_cgpa))
print(id(s_cgpa))

# int flot are immutabel data

#define some complex data types
#list is mutabel data types
list_1=[1,2,3]
list_2=[1,2,3]
print(id(list_1))
print(id(list_2))



x="p"
y="q"
z="r"
print(x+y+z) # string concatenation

x=10
y=20
print(x+y)  #Addition operator
#z= "p" 
#print(x+z) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

x,y,z ="one", "two", "three"
print(x+y+z)

x=y=z="one"
print(x)
print(y)
print(z)