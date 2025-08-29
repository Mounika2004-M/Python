# TASK - Rewrite the LMS DS App with below implementation

#         -> if choice == "1":
#             add_student()

#         -> if choice == "2":
#             update_student()
        
#         -> Implement a new option to work a search criteria, where search students 
#             should displayed based if has that skill

#             print("4 - List All Students")
#             print("5 - Search")    
#             print("6 - Exit System")  

#             -> NOTE - Use lambda based approach 
STUDENT_INFO = ("LMS Students Portal","v1.0","2025","Edify University")
ADMIN_INFO = ("mouni@gmail.com","7406934523","29")

print("="*50)
print(f"Welcome {STUDENT_INFO[0]} ")
print(f"Developed by {STUDENT_INFO[3]} ")
print("="*50)

students={}
def add_student():
    student_id=input("Enter student Id: ")
    if student_id in students:
             print("This student id is already exist")
    else:
        name = input("Enter the student name: ").title()

        scores=[]
        while True:
            score_input=input("Enter the score or done: ") 
            if score_input == "done"  :
                    break
            if score_input.isdigit():
                    score=int(score_input)
                    if 0<=score<=100:
                        scores.append(score)
                    else:
                        print("Enter the numbers between 1-100")
            else:
                    print("Enter the numbers only")   

        
        skills=set()
        while True:
            skill_input=input("Enter the skills or done: ") 
            if skill_input == "done"  :
                break
            skills.add(skill_input.strip().title())

        # save student details received so far
        students[student_id]= {
            "name":name,
            "scores":scores,
            "skills":skills
        }
        print("Student Added Successfully!")
            
            # For Verification print student
        print(students)

def modify_student():
        print("perforem the 2 st operation")
        # Modify Student Name
        student_id=input("Enter the student ID :")
        if student_id in students:
            new_name = input("Enter the new name :").title()
            students [student_id]["name"] = new_name
            print("Student updeate sucussfull")
        else:
            print("The student Id not exist ")
        print(students)

def delete_student():
        print("perforem the 3 st operation")
        student_id=input("Enter the Id to delete")
        removed=(dict(filter(lambda  student_id : students.pop(student_id,None),  students())))
        if removed:

            print("The student removed succussfully")
        else :
            print("The student not  removed ")
        print(students)

def listAllStudent():
        print("Performing Operation 4")
        # id - student_id
        # skills 
        # scores
        # students
        if not students:
            print("No Students Available")
        else:
            print("="*50)
            print("Students Details")
            print("="*50)
            
            for sid, data in students.items():
                name = data["name"]
                scores = data["scores"]
                
                if scores:
                    avg = sum(scores)/len(scores)
                else:
                   avg = 0
                
                if scores:
                    top_score = max(scores)  
                else:
                    top_score = 0    
                
                skills = data["skills"]
                print(f"ID: {sid}")
                print(f"Name: {name}")
                print(f"Scores: {scores}")
                print(f"Average Score: {avg}")
                print(f"Top Score: {top_score}")
                print(f"Skills: {skills}")
                print(f"Skills Count: {len(skills)}")
    
def search_student_by_skill():
    print("Performing Search Operation")
    skill = input("Enter the skill to search: ").title()

    matched_skill=dict(filter(lambda item: skill in item[1]["skills"], students.items()))
    if matched_skill:
        print(f"Students having skill '{skill}':") 
        for sid, data in matched_skill.items():
            print(f"ID: {sid} | Name: {data['name']} | Skills: {data['skills']}")
             
    else:
         print("skill is not found")

def Admincontact():
         print("perforem the 5 st operation")
         print("Performing operation 5")
         print("="*50)
         print("Contact Admin for further queries")
         print(f"Admin contact:{ADMIN_INFO[1]}")
         print(f"Admin contact:{ADMIN_INFO[0]}")
         print("="*50)

while True:
    print("Choose an option from (1-5): ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List All Students")
    print("5-serach related skill students")
    print("6 - Exit System")

    choice =  input("Enter your choice: ")
    if choice == "1":
         print(add_student())
    elif choice =="2":
         print(modify_student())
    elif choice == "3":
         print(delete_student())
    elif choice == "4":
         print(listAllStudent())
    elif choice== "5":
         print(search_student_by_skill())
    elif choice == "6":
         print(Admincontact())
    else:
         print("invalid choice")


