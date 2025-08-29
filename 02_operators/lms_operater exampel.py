student_iD = 29
student_name = "Mounika"
student_age =20
quiz_score = 85
assignment_score = 90
exam_score =98
student_attendance = 98

#Use arithmetic operators to calculate:
#Total score
#Average score

total_score= quiz_score+assignment_score+exam_score 

average_score=total_score/3

#Use relational operators to determine:
#If the student is passing based on average score 75

student_passed=average_score>=75

# Use increment operator to update:
# Attendance (simulate an additional attended session)
student_attendance +=1

#Use logical operators to determine award eligibility:
#the student qualifies for an award (requires high attendance i.e 90 and above and a passing grade)

award_eligibility = student_attendance>=90 and student_passed

print(f"The student name {student_name}")
print(f"Total score is {total_score}")
print(f"average scoreis  {average_score}")
print(f"student passed {student_passed}")
print(f"award eligibility {award_eligibility}")






