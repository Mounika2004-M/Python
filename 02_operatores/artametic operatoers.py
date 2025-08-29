#Arthemetic opertoers

num1 = 10
num2 = 20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1//num2)
print(num1**num2)

# Compound Operatoers
num = 10
num +=6
print(num)
num -=6
print(num)
num *=6
print(num)
num /=6
print(num)
num %=11
print(num)
num //=6
print(num)
num **=10
print(num)

#Comperision/relational operatoers

num1 = 10
num2 = 20
print(num1<num2)
print(num1!=num2)
print(num1==num2)

# Logical operatoers
a=10
b=4
c=6
d=8
result=a<c and c<d
print(result)
result=a<c or c<d
print(result)
result=c<d
print(not result)

#membership operatoers
text = "python is good"
is_m_present = "m" in text
print(is_m_present)

list = [1,3,5]
is_7_present= 7 in list
print(is_7_present)

list = [1,3,5,7]
is_7_present= 7 in list
print(is_7_present)

#identity operatoers
num1_list=[10,20]
num2_list=[10,20]
print(type(num1_list))
print(id(num1_list))
print(type(num2_list))
print(id(num2_list))
print(num1_list is num2_list)
print(num1_list is not num2_list)

#Bitwise operatoers
a = 5 # 0000000000000101
b = 3 # 0000000000000011
resultand = a & b # 0000000000000001
print(resultand)

resultor = a | b # 0000000000000111
print(resultor) 

resultxor = a ^ b # 0000000000000110
print(resultxor) 

resultnot = ~b
print(resultnot) # 0000000000000011 -> 1111111111111100

b = 3 # 0000000000000011
print(3<<2) # 0000000000001100 --> 12
print(3<<1) # 0000000000000110 --> 6
print(3<<3) # 0000000000011000 --> 24

b = 3 # 0000000000000011
print(3>>2) # 0000000000000000 --> 0
print(3>>1) # 0000000000000001 --> 1
print(8>>2) # 0000000000001000 --> 0000000000000010

# c = -4 # 1111111111111111
print(-4>>3) # 1111111111111111

