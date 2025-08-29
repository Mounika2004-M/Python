# studetname=input("enter student name:")
# grade=int(input("Enter student Grade(1-12):"))
# discount_percentage= 0.0

# if grade < 1 and grade > 12:
#     print("Invalid Grade. Please enter a grade between 1 and 12.")
# else:
#     print("Valid Grade")
#     base_tuition_fee = int(input("Enter Base Tuition Fee: "))
#     topper = input("Is the student an academic topper? (yes/no): ").lower()

#     # Determine base discount
#     if grade >= 9 and grade <= 12:
#         if topper == "yes":
#             discount = 20 
#         else: 
#             discount = 10
#     elif grade >= 6 and grade <= 8:
#         discount = 5
#     else:
#         discount = 0

#     discount+=discount_percentage

#     extra_discount =0
#     match grade:
#         case 10:
#             extra_discount = 3
#         case 12:
#             extra_discount = 5
        
#         case _:
#               extra_discount = 0

#     total_discount = discount + extra_discount
#     discount_amount = (total_discount / 100) * base_tuition_fee
#     final_fee = base_tuition_fee - discount_amount
#     print(f"Student Name        :{studetname}")
#     print(f"Grade             :{ grade}")
#     print("Academic Topper     :", "Yes" if topper == "yes" else "No")
#     print(f"Base Fee            : {base_tuition_fee}")
#     print(f"Total Discount %    :{total_discount}")
#     print(f"Discount Amount     : ₹{discount_amount}")
#     print(f"Final Tuition Fee   : ₹{final_fee}" )


std_name=str(input("Enter the student name:"))
std_grade=int(input("Enter the grade:"))
tuition_fee=int(input("Enter the tuition fee:"))
discount_per=0

if std_grade>=1 and std_grade<=12:
    print("Valid")
else:
    print("Invalid")
academic_topper = input("Is the student an academic topper? (yes/no): ").strip().lower()
if std_grade>=9 and std_grade<=12:
    if academic_topper=="yes":
        discount_per+=20   
    else:
        discount_per+=10
elif std_grade<=6 and std_grade>=8:
    discount_per+=5  
elif std_grade<6:
    print("No discount")
else:
    print("Invalid")
match std_grade:
    case 10:
        discount_per+=3
    case 12:
        discount_per+=5
    case _:
        pass
discount_amount=(tuition_fee*discount_per)/100
final_fee=tuition_fee-discount_amount

print("Student name:",std_name)
print("Student grade:",std_grade)
print("Academic topper:",academic_topper)
print("Tuition fee:",tuition_fee)
print("Discount:",discount_amount)
print("Final Tuition fee after discount:",final_fee)
            







 











