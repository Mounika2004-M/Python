import random
otp=random.randint(1000,9999)
print(otp)
attempts=3
while attempts:
    user_input=int(input("enter 4 digit otp: "))
    if len(str(user_input)) !=4:
        print("Invalid OTP! Please enter a 4-digit OTP.")
    if user_input == otp:
        print("OTP verified successfully!")
        break
    attempts -= 1
else:
    print("Maximum attempts reached. OTP verification failed.")

i=input("10")
print(type(i))

if 10=="10":
    print("equal")
else:
    print("not equal")

                 
   

    
    