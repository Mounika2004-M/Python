car_name="Mahindra"
actual_price = 1753690
down_payment = 160000
interest_rate = 9.0
loan_years = 5
loan_amount = actual_price - down_payment

# Calculate EMI components
R = interest_rate / (12 * 100)  # Monthly interest rate
N = loan_years * 12             # Loan period in months

# EMI formula
EMI = loan_amount * R * (1 + R) ** N / ((1 + R) ** N - 1)
total_payable = EMI * N

# Output
print(f"Car Name: {car_name}")
print("actual_price: ₹", round(actual_price,2))
print("Loan Amount: ₹", round(loan_amount,2))
print("Monthly EMI: ₹", round(EMI,2))
print("Total Payable Amount: ₹", round(total_payable))