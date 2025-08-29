# 1==> Positional Arguments 
def login(username,password):
    if username == "ravi" and password == "12345":
        print("Login Success")
    else:
        print("Login Failed")

student1=login("ravi","12345") # exact order
login("ravi","123") # exact order //login failed
login("12345","ravi") # order changed // login failed

# Default Arguments 
def emp_info(emp_name,emp_email,emp_loc="Hyderabad",address="India"):
    print(f"Hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {address}")

# emp_info("Ravi","ravi@gmail.com","Hyderabad")
emp_info("Krishna","krishna@gmail.com")
emp_info("user3","user3@gmail.com")
emp_info("user4","Bangalore","user3@gmail.com")
emp_info("user5","user5@gmail.com","Pune","USA")

# Keyword Arguments 
def emp_info(emp_name,emp_email,emp_loc,address="India"):
    print(f"Hi {emp_name} your email is {emp_email} and location is {emp_loc} actually from {address}")

emp_info(emp_name="mounika",emp_loc="Bangalore",emp_email="user3@gmail.com")

# Arbitrary Positional Arguments
def add_all(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print(f"Total is: {total}")

add_all()
add_all(1)
add_all(1,2)
add_all(1,2,3,4,5,6,7,8,9)



# Arbitrary Keyword Arguments (**kwargs) 
def profile(**info):
    print(info)

profile()
profile(id="101")
profile(id="102",name="Ravi")
profile(id=102,name="Ravi",rating=4.5)

# transaction exampel
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        total = total + trans[i]
    print(f"You have done {len(trans)} and total value of all transactions is {total}")
cred_trans(jan=1000, feb=2000, mar=3000)        


def cred_trans_new(*trans, **info):
    print(trans)
    print(info)
    total = 0
    for i in trans:
        total = total + i
    print(f"Hi {info['name']} you have done {total} amount of transactions ")

cred_trans_new(1000,3000,5000,name="Ravi",email="ravi@gmail.com")


