# without using return keyword
def add(a,b):
    a+b
print(add(10,20)) #None


# with return keyword ==> when we using return it gives the apprapriate message
def add(a,b):
   return a+b
print(add(10,20))# 30

# multipel return keyword
def  arthamatic(a,b):
    return a-b
    return a+b
    return a*b
print( arthamatic(10,20)) # -10 it exicute only first return ststement
print( arthamatic(10,20))  # -10

# we also using multipel returns but logic shold be apprapriate
def math_opr(a,b,opr):
    if opr=="+":
        return a+b
    elif opr=="-":
        return a-b
    elif opr=="*":
        return a*b
    elif opr=="/":
        return a/b
    else:
        return "invalid operatoer"
print(math_opr(3,4,"+"))#7
print(math_opr(3,4,"-"))#-1
print(math_opr(3,4,"*"))#12
print(math_opr(3,4,"/"))#0.75
print(math_opr(3,4,"."))#inalid operatoer

# Local scope for variabel

def add():
    #local Varibels
    c=5
    d=4
    print(d) # accessing inside the function  o/p==4
    print(c) # accessing inside the function  o/p==5
add()

# print(c) #name 'c' is not defined  //accessing outside the function


# parameters passed to function are also local varibels

def add(m,n):
    print(m)
    print(n)
add(10,20)  #20
#print(n) #NameError: name 'n' is not defined


#Global Scope
aa=30
def add(bb,cc,aa):
    print(bb)
    print(cc)
    print(aa)
    print(globals()['aa'])
add(8,9,6)
print(aa) #30 #accssing outside the function
#print(bb)#NameError: name 'bb' is not defined

# try to change global varibel
count=0
def increment():
    #count+=1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    global count
    count+=1
increment()
print("count: ",count) #count:  1

# function composition 
def add(a,b):
    return a+b

def sub(c,d,e):
    return  add(c,d)-e

print(sub(3,4,5)) # 2

def new_fun(name, **info):
    pass





