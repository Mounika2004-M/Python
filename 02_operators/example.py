student_name = input("Enter student name: ")
grade = int(input("Enter student Grade (1-12): "))

if grade < 1 or grade > 12:
    print("Invalid grade! Please enter grade between 1 to 12.")

else:
    base_tuition_fee = int(input("Enter Base tuition fee: "))
    discount_percentage = 0.0
    topper = input("The student an academic topper (yes/no): ")
    if grade >= 9 and grade <= 12:
        if topper == "yes":
            discount = 20
        else:
            discount = 10

    elif grade >= 6 and grade <= 8:
        discount = 5
    else:
        discount = 0    

    discount += discount_percentage
    extra_discount = 0
    match grade:    
        case 10:
            extra_discount += 3
        case 12:
            extra_discount += 5
        case _:
            extra_discount += 0
    total_discount = discount + extra_discount
    discount_amount = (total_discount / 100) * base_tuition_fee
    final_fee = base_tuition_fee - discount_amount
    print("\n----- Tuition Fee Summary -----")
    print(f"Student Name        : {student_name}")      
    print(f"Grade               : {grade}")
    print("Academic Topper     :", "Yes" if topper == "yes" else "No")
    print(f"Base Fee            : ₹{base_tuition_fee}")
    print(f"Total Discount %    : {total_discount}")
    print(f"Discount Amount     : ₹{discount_amount}")
    print(f"Final Tuition Fee   : ₹{final_fee}")
    
    
