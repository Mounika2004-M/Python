studetname=input("enter student name:")
grade=int(input("Enter student Grade(1-12):"))

if  grade>=1 and grade <= 12:
    print("Valid Grade")
    base_tuition_fee=int(input("Enter Base tuition fee: "))
    topper = input("Is the student an academic topper? (yes/no): ").strip().lower()
    discount_percentage= 0.0
    if  grade>=9 and grade <= 12:
        if topper == "yes":
            discount = 20
        else:
            discount = 10
    elif grade >= 6 and grade <= 8:
        discount = 5
    else:
        discount = 0
    discount+=discount_percentage

    extra_discount =0
    match grade:
        case 10:
            extra_discount = 3
        case 12:
            extra_discount = 5
        
        case _:
              extra_discount = 0

    total_discount = discount + extra_discount
    discount_amount = (total_discount / 100) * base_tuition_fee
    final_fee = base_tuition_fee - discount_amount
    print(f"Student Name        :{studetname}")
    print(f"Grade             :{ grade}")
    print("Academic Topper     :", "Yes" if topper == "yes" else "No")
    print(f"Base Fee            : {base_tuition_fee}")
    print(f"Total Discount %    :{total_discount}")
    print(f"Discount Amount     : ₹{discount_amount}")
    print(f"Final Tuition Fee   : ₹{final_fee}" )
            

else:
    print("Invalid Grade. Please enter a grade between 1 and 12.")





 











