student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

attendence=int(input("Enter attendance percentage: "))
if attendence<=75:
    attendence_status = ("warning - Low Attendence")
else:
    attendence_status = ("ok attendence satisified")
    
total_score=0
num_subjects = 0
sub_num = 1

while True:
    score_input=int(input(f"Enter marks for Subject{sub_num} :"))
    if score_input>0 and score_input<=100:
        total_score+= score_input
        num_subjects += 1
        sub_num += 1
        continue_input = input("Do you want to enter another score? (yes/no): ")
        if continue_input != "yes":
          break
    else:
        print("Invalid score! Please enter a score between 0 and 100.")
        
if num_subjects > 0:
    average_score = total_score / num_subjects
else:
    average_score = 0

        
if  average_score >=85:
    Performance=("excellent")
elif average_score >=74 and average_score <= 85:
    Performance=("good")
elif average_score >=50 and average_score <= 69:
  Performance=("Average")
else:
    Performance=("need to improvement")

print(f"Student Id: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student attendance:{attendence}%")
print (f"Total score:{total_score}")    
print (f"Total Number of subjects:{num_subjects}")
print(f"Average score:{average_score}")
print(f"Performance: {Performance}")
print(f"Attendance: {attendence_status}")



    

  
