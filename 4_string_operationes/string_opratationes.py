print("="*30)
print("Enhanced LMS Grade Tracker")
print("="*30)

#validate id
student_id_valid=False
while not student_id_valid:
    student_id=input("Enter your id: ")
    #check  if valid id based on - sign
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please enter the positive va;lues")
    elif student_id.isdigit():
        student_id=int(student_id)
        if student_id>0:
            student_id_valid=True
        else:
            print("please enter the non zero values")
    else:
        print("Enters numbers only")
print(student_id)

#formate id
formatted_id = "STU" + str(student_id).zfill(5)
print(formatted_id)
        

#validate name
student_name_valid=False
while not student_name_valid:
    student_name=input("Enter your name: ")
    student_name=student_name.strip().title()
#name check should have only alphebets
    name_check=student_name.replace(" ","")
    if name_check.isalpha and len(student_name)>=3:
        student_name_valid=True
        print(name_check)

#Email Validation
name_part=student_name.split()
first_name=name_part[0].lower()
student_email=first_name+"."+str(student_id)+"@university"+"."+"edu"
print(student_email)
