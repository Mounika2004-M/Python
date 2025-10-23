# 1-built in function
# 2-userDefined function
# 3-lambda function

# built function in python
print(dir(__builtins__))

#built in function
text="python"
len_text=len(text)
print(len_text)

# simulate len with our way
def user_def_len(s):
    count=0
    for cahr in s:
        count+=1
    return count
print(user_def_len("phy")) #3

#Lambda function(anonymous function) ===> its one line function means only singel line expression
# we use lambda keyword and result of the expression is automatically returned

# Syntax 
   #  lambda arguments: expression  note: arguments can be multipel but expreesion only one line


#without lambda
def add(a,b):
    return a+b
print (add(3,4))


#with lambda ====> this one way
sum=lambda a,b: a+b
print(sum(5,90))


# with lambda ==> another way is "IILE(immediatly invoked lambda functiones)"
print((lambda a,b: a+b) (80,90))
print((lambda a,b: a+b) (880,90))
 
